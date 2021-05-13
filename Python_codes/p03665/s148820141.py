N,P=list(map(int, input().split()))
A=list(map(int, input().split()))

# たぶん普通にDP
# dp[i]:i番目(1-index)までの袋から偶奇が正しくなるように選ぶ場合の数

dp=[0]*(N+2)
dp[0]=(P+1)%2

for i in range(1,N+1):
    if A[i-1]%2==0:
        dp[i]=2*dp[i-1]
    else:
        dp[i]=(2**(i-1)-dp[i-1])+dp[i-1]
print(dp[N])