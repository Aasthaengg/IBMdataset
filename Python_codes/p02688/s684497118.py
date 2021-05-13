import itertools
n,k = (int(x) for x in input().split())
a = []
l = []

for i in range(k):
    d = int(input())
    a.append(list(map(int, input().split())))
b = list(itertools.chain.from_iterable(a))

for i in range(1,n+1):
    l.append(i)

ans = set(b)^set(l)
print(len(set(ans)))