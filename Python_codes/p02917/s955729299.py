N = int(input())
B = list(map(int,input().split()))

dp = [10**8]*N
for i in range(N-1):
    if dp[i]>B[i]:
        dp[i]=B[i]
    if dp[i+1]>B[i]:
        dp[i+1]=B[i]
    
print(sum(dp))