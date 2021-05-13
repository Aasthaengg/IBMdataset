def f():
    import sys
    input=sys.stdin.readline
    n,m=[int(i) for i in input().split()]
    s=[int(i) for i in input().split()]
    t=[int(i) for i in input().split()]
    mod=10**9+7
    dp=[[0]*(m+1) for i in range(2)]
    dp[0][0]=1
    for i in range(n+1):
        for j in range(m+1):
            if i!=0:
                dp[i%2][j]=dp[(i-1)%2][j]
            if j!=0:
                dp[i%2][j]+=dp[i%2][j-1]
            if i!=0 and j!=0:
                if s[i-1]!=t[j-1]:
                    dp[i%2][j]-=dp[(i-1)%2][j-1]
            dp[i%2][j]%=mod
    print(dp[n%2][m])


f()


