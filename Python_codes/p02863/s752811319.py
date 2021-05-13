from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,t=map(int,readline().split())
    li=[list(map(int,readline().split())) for _ in range(n)]
    li.sort()
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=li[i][0],li[i][1]

    #ナップサックDP
    inf=-10**9
    dp=[[inf]*(t+1) for _ in range(n+1)]
    dp[0][0]=0
    for i in range(n):
        for j in range(t+1):
            #i番目を食べる
            if j!=t:
                dp[i+1][min(t,j+a[i])]=max(dp[i+1][min(t,j+a[i])],dp[i][j]+b[i])
            
            #i番目を食べない
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])

    print(max(dp[n]))

if __name__=="__main__":
    main()