def fun(a):
    if len(a)==1:
        return 0
    dp = [0]*len(a)
    dp[0]=a[0]
    dp[1]=dp[0]+abs(a[0]-a[1])
    for i in range(2,len(a)):
        dp[i]=min(dp[i-1]+abs(a[i]-a[i-1]) ,dp[i-2]+abs(a[i]-a[i-2]))
    return dp[-1]-a[0]
  
n = int(input())
a = list(map(int , input().split()))
print(fun(a))