import itertools
N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]

ab = list(itertools.chain.from_iterable(ab))

for x in range(1, N + 1):
    print(ab.count(x))