def main():
    n,m=map(int,input().split())
    c=list(map(int,input().split()))
    dp=list(range(n+1))
    k=0
    while k<len(c):
        for i in range(n+1-c[k]):
            dp[i+c[k]]=min(dp[i+c[k]],dp[i]+1)
        k+=1
    print(dp[n])

if __name__=="__main__":
    main()
