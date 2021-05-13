import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w,k = map(int,input().split())
k -= 1

dp = [[0]*w for _ in range(h+1)] # 横棒i本のときの0->jに至るくじ

dp[0][0] = 1

d = {}
M = 10**9+7
def sub(i):
    # i本棒がある区間の横棒の入れ方
    if i in d:
        return d[i]
    if i<=1:
        ans = 1
    else:
        ans = sub(i-1) + sub(i-2)
    ans %= M
    d[i] = ans
    return ans
    

for i in range(1,h+1):
    for j in range(w):
        if j>=1:
            dp[i][j] += dp[i-1][j-1]*sub(j-1)*sub(w-j-1)
        if j<=w-2:
            dp[i][j] += dp[i-1][j+1]*sub(j)*sub(w-j-2)
        dp[i][j] += dp[i-1][j]*sub(j)*sub(w-j-1)
        dp[i][j] %= M
print(dp[h][k])