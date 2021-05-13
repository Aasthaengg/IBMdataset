n = int(input())
F = [tuple(map(int, input().split())) for _ in range(n)]
P = [tuple(map(int, input().split())) for _ in range(n)]

ans = -10**12
from itertools import product
for i in range(1, 2**10):
    pattern = [(i>>j)&1 for j in range(10)]
    rieki = 0
    for ff, pp in zip(F, P):
        count = sum([f and p for f, p in zip(ff, pattern)])
        rieki += pp[count]

    ans = max(ans, rieki)
print(ans)
