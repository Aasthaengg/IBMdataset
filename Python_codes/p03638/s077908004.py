from itertools import chain, islice

h, w = map(int, input().split())
n = int(input())
a = map(int, input().split())
c = chain.from_iterable([i] * ai for i, ai in enumerate(a, 1))

for i in range(h):
    l = list(islice(c, 0, w))
    if i % 2 == 1:
        l.reverse()
    print(*l)
