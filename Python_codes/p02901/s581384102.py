from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,m=map(int,readline().split())
    a=[0]*m
    b=[0]*m
    c=[0]*m
    for i in range(m):
        a[i],b[i]=map(int,readline().split())
        li=list(map(int,readline().split()))
        for j in range(len(li)):
            c[i]|=1<<(li[j]-1)

    inf=10**9
    dp=[[inf]*(1<<n) for _ in range(m+1)]
    dp[0][0]=0
    for i in range(1,m+1):
        for j in range(1<<n):
            #i番目の鍵を使わない
            dp[i][j]=min(dp[i-1][j],dp[i][j])

            #i番目の鍵を使う
            dp[i][j|c[i-1]]=min(dp[i][j|c[i-1]],dp[i-1][j]+a[i-1])

    ans=dp[m][(1<<n)-1]
    print(ans if ans<inf else -1)

if __name__=="__main__":
    main()