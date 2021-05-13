import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

n = int(readline())
ab = [list(map(int,readline().split())) for i in range(n)]
ab.sort(key=lambda x: -x[0]-x[1])
ans = 0
for i in range(n):
    if i%2:
        ans -= ab[i][1]
    else:
        ans += ab[i][0]
print(ans)

