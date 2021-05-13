def fun(a,k,n): ## k different steps can be taken
    if n==1:
        return 0
    dp = [0]*n
    dp[1]=dp[0]+abs(a[0]-a[1])
    for i in range(2,len(a)):
        t = 0
        min_ = float('inf')
        for j in range(i-1,-1,-1):
            if t==k:
                break
            else:
                t+=1
            if dp[j]+abs(a[i]-a[j]) < min_ :
                   min_ = dp[j]+abs(a[i]-a[j])
        dp[i]=min_
    return dp[-1]
from sys import stdin , stdout
n,k = map(int , stdin.readline().split())
a = list(map(int , stdin.readline().split()))
print(fun(a,k,n))