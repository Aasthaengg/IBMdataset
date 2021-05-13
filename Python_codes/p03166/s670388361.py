import sys
sys.setrecursionlimit(10**6)
def f(x):
    if flg[x]:
        flg[x] = 0
        p = 0
        for y in glaph[x]:
            p = max(p,f(y)+1)
        dp[x] = p
    return dp[x]
n,m = map(int,input().split())
flg = [1]*(n+1)
dp = [0]*(n+1)
glaph = [[] for i in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    glaph[x].append(y)
ans = 0
for i in range(1,n+1):
    ans = max(ans,f(i))
print(ans)
