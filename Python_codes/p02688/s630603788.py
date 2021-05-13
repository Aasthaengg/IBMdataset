import itertools

N, K = map(int, input().split())

d = []
a = []

for i in range(K):
    d.append(int(input()))
    a.append(list(map(int, input().split())))

a = itertools.chain.from_iterable(a)
b = set(a)

print(N - len(b))
