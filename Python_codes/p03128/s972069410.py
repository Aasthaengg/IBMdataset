#118_D
ch={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

n,m=map(int,input().split())
a=list(map(int,input().split()))

dp=[-1 for _ in range(n+1)]
dp[0]=0
for i in range(1,n+1):
    res=-1
    for x in a:
        if i-ch[x]>=0:
            res=max(res,dp[i-ch[x]]*10+x)
    dp[i]=res
    
print(dp[n])