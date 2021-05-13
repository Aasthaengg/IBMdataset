#

import sys
input=sys.stdin.readline

def main():
    N,K=map(int,input().split())
    # gcd=i
    dp=[0]*(K+1)
    MOD=10**9+7
    for i in range(K,0,-1):
        x=(K//i)
        dp[i]=pow(x,N,MOD)
        # (x**N)%MOD、pow(x,N)%MODはTLEE
        for j in range(2,x+1):
            dp[i]-=dp[i*j]
            dp[i]%=MOD
    ans=0
    for i in range(K+1):
        ans+=i*dp[i]
        ans%=MOD
    print(ans)
    
    
    
if __name__=="__main__":
    main()
