#メモ化再帰
N,W = map(int,input().split())
WV = [list(map(int,input().split())) for _ in [0]*N]
memo = [{} for _ in [0]*(N+1)]
def dp(i,j):
    if j<=0 or i<=0: return 0
    if j in memo[i]:return memo[i][j]
    w,v = WV[i-1]
    ret = dp(i-1,j)
    if j-w>=0: ret = max(ret,dp(i-1,j-w)+v)
    memo[i][j] = ret
    return ret
print(dp(N,W))