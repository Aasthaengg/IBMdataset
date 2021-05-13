def main():
    INF=10**9
    n,m=map(int,input().split())
    key=[0]*m
    keycost=[0]*m

    for i in range(m):
        a,b=map(int,input().split())
        keycost[i]=a
        c=[pow(2,int(i)-1) for i in input().split()]
        key[i]=sum(c)
    
    dp=[[INF]*(m+1) for _ in range(1<<n)]
    dp[0]=[0]*(1+m)
    
    for s in range(1<<n):
        for i in range(m):
            dp[s][i+1]=min(dp[(s&key[i])^s][i]+keycost[i],dp[s][i])
    
    if dp[-1][m]==INF:
        print(-1)
    else:
        print(dp[-1][m])
 
if __name__=='__main__':
    main()