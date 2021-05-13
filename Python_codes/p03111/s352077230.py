n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

from itertools import product
ptns = list(product([0,1,2,-1], repeat = n))

ans = 10**9
for i in range(len(ptns)):
    if 0 not in ptns[i] or 1 not in ptns[i] or 2 not in ptns[i]:
        continue
    abc = [0, 0, 0, -30]
    for j in range(n):
        tmp = ptns[i][j]
        if tmp >= 0:
            abc[tmp] += l[j]
            abc[3] += 10
    mp = abc[3]
    mp += abs(abc[0] - a)
    mp += abs(abc[1] - b)
    mp += abs(abc[2] - c)
    ans = min(ans, mp)

print(ans)