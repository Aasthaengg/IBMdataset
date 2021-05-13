#import  sys
#input=sys.stdin.readline
#sys.setrecursionlimit(1000000)
mod=int(1000000007)
#I=lambda: map(int,input().split())

def bm(n,p):
    n,p=int(n),int(p)
    if p==0:
        return 1
    x=bm(n,p/2)
    x=(x*x)%mod
    if p%2==1:
        x=(x*n)%mod
    return x

dp=[0]*(100000+2)
ans=0
n,k=map(int,input().split())

for i in range(k,0,-1):
    dp[i]=bm(k/i,n)
    for j in range(i*2,k+1,i):
        dp[i]=(dp[i]-dp[j]+mod)%mod
    ans=ans+dp[i]*i;
    ans%=mod
print(ans)
