n=int(input())

dp=[1,1]
def fib(n):
    if n==0 and n==1:
        return dp[n]
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]
print(fib(n))

