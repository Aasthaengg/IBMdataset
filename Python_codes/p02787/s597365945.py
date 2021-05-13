#

import sys
input=sys.stdin.readline
MOD=10**9+7

def main():
    H,N=map(int,input().split())
    AB=[list(map(int,input().split())) for i in range(N)]
    dp=[10**9]*(H+1+10**4)
    dp[0]=0
    for i in range(H+10**4):
        for j in range(N):
            if 0<=i+AB[j][0]<=H+10**4:
                dp[i+AB[j][0]]=min(dp[i+AB[j][0]],dp[i]+AB[j][1])
    ans=10**9
    for i in range(H,H+1+10**4):
        ans=min(ans,dp[i])
    print(ans)
    
        
    
if __name__=="__main__":
    main()
