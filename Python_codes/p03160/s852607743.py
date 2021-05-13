#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))
  
n=int(input())
H=input_array()
INF=10**9
# 最小化問題
dp=[INF]*n
# 初期化
dp[0]=0

for i in range(1,n):
	a=dp[i-1]+(abs(H[i]-H[i-1]))
	b=dp[i-2]+(abs(H[i]-H[i-2]))
	dp[i]=min(a,b)
print(dp[n-1])