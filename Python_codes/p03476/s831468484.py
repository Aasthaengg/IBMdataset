def erat(M):
    p = [1] * M
    p[0] = p[1] = 0
    for x in range(2, int((M - 1)**.5) + 1):
        if p[x]:
            for y in range(x*x, M, x):
                p[y] = 0
    return p
INF = 10**5 + 1
p = erat(INF)
q = [0] * INF
from itertools import*
for i in range(INF):
    q[i] = i%2 * p[i] * p[-~i//2]
*a, = accumulate([0] + q)
for _ in [None] * int(input()):
    l, r = map(int, input().split())
    print(a[-~r] - a[l])
