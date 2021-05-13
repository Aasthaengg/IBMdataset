from operator import mul
from itertools import starmap

n, m, l = map(int, input().split())
a, b = ([tuple(map(int, input().split())) for _ in range(k)] for k in (n, m))
for line in ([sum(starmap(mul, zip(ai, bj))) for bj in zip(*b)] for ai in a):
    print(*line)