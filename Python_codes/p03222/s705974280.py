h,w,k = map(int,input().split())
mod = 10**9+7
dp = [0]*(w+2)
dp[1] = 1

#左右の余白を埋めるパターン数
ref = [1,2,3,5,8,13,21]
pat = lambda l,r:ref[max(l,0)] * ref[max(r,0)]

for i in range(h):
	_dp = [0]*(w + 2)
	for j in range(1,w+1):
		_dp[j] = dp[j-1]*pat(j-3,w-j-1) + dp[j]*pat(j-2,w-j-1) + dp[j+1]*pat(j-2,w-j-2)
		_dp[j] %= mod
	dp = _dp
print(dp[k])