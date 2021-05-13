import sys
input = sys.stdin.readline

n=int(input())
L=list(map(int,input().split()))

dp = [1000]*n

for i in range(n):
    dp[i]=max(dp[i-1],dp[i])
    st,rest=divmod(dp[i],L[i])
    for j in range(i+1,n):
        dp[j] = max(dp[j],L[j]*st+rest)
print(dp[-1])

    
        
        
