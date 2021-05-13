h,w,k = map(int,input().split())
mod = 10**9+7
dp = [[0]*(w+2) for _ in range(h+1)]
dp[0][1] = 1

#左右の余白を埋める場合の数
ref = [1,2,3,5,8,13,21]
pat = lambda l,r:ref[max(l,0)]*ref[max(r,0)]

for i in range(h):
	for j in range(1,w+1):
		dp[i+1][j] = dp[i][j-1]*pat(j-3,w-j-1) + dp[i][j]*pat(j-2,w-j-1) + dp[i][j+1]*pat(j-2,w-j-2)
		dp[i+1][j] %= mod
print(dp[-1][k])