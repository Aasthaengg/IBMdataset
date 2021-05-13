
import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)

N, M = map(int,input().split())
xy = [list(map(int,input().split())) for _ in range(M)]

indeg = [0 for _ in range(N)]
outdeg = [[] for _ in range(N)]

for x, y in xy:
    x,y = x-1, y-1
    indeg[y] += 1
    outdeg[x].append(y)

heads = []
for i in range(N):
    if not indeg[i]:
        heads.append(i)

dp = [0 for _ in range(N)]
while heads:
    h = heads.pop()
    for c in outdeg[h]:
        dp[c] = max(dp[c], dp[h]+1)
        indeg[c] -= 1
        if indeg[c] == 0:
            heads.append(c)
#        print(h,c,dp)

ans = max(dp)
print(ans)