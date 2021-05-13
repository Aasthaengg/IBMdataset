def resolve():
    #n=int(input())
    #a,b=map(int,input().split())
    #x=list(map(int,input().split()))
    #a=[list(map(lambda x:int(x)%2,input().split())) for _ in range(h)]
    n,k=map(int,input().split())
    MOD=998244353
    lr=[list(map(int,input().split())) for _ in range(k)]
    dp=[0]*(n+1)
    dpsum=[0]*(n+1)
    dp[1]=1
    dpsum[1]=1
    for i in range(2,n+1):
      for l,r in lr:
        li=i-r
        ri=i-l
        if r<0:continue
        li=max(1,li)
        dp[i]+=dpsum[ri]-dpsum[li-1]
      dpsum[i]=(dpsum[i-1]+dp[i])%MOD
    print(dp[n]%MOD)
    
if __name__ == '__main__':
    resolve()