from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n,c=map(int,readline().split())
    x=[0]*n
    v=[0]*n
    for i in range(n):
        x[i],v[i]=map(int,readline().split())

    x_rev=list(map(lambda x:c-x,reversed(x)))
    v_rev=list(reversed(v))

    dp=[0]*(n+1)
    dp_rev=[0]*(n+1)
    now=0
    tmp=0
    for i in range(n):
        dp[i+1]=max(dp[i],tmp+v[i]-x[i]+now)
        tmp+=v[i]-x[i]+now
        now=x[i]
    now=0
    tmp=0
    for i in range(n):
        dp_rev[i+1]=max(dp_rev[i],tmp+v_rev[i]-x_rev[i]+now)
        tmp+=v_rev[i]-x_rev[i]+now
        now=x_rev[i]

    ans=0
    #時計、反時計
    for i in range(n):
        tmp1=dp[i+1]
        tmp2=dp[i+1]-x[i]+dp_rev[n-i-1]
        ans=max(ans,tmp1,tmp2)

    #反時計、時計
    for i in range(n):
        tmp1=dp_rev[i+1]
        tmp2=dp_rev[i+1]-x_rev[i]+dp[n-i-1]
        ans=max(ans,tmp1,tmp2)

    print(ans)

if __name__=="__main__":
    main()