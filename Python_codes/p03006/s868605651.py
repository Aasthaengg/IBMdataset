import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import defaultdict
mod = 10**9+7

N = int(input())
xy = [list(map(int, input().split())) for i in range(N)]
xy.sort()
Ans = N
for i in range(N):
    for j in range(i+1, N):
        a, b = xy[j][0]-xy[i][0], xy[j][1]-xy[i][1]
        ans = N
        for k in range(N):
            for l in range(k+1, N):
                if xy[k][0]+a == xy[l][0] and xy[k][1]+b == xy[l][1]:
                    ans -= 1
        Ans = min(Ans, ans)
print(Ans)
