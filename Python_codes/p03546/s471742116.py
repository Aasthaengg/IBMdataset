# ABC079

import sys
input=sys.stdin.readline

def main():
    inf=10**6
    H,W=map(int,input().split())
    dp=[[inf]*10 for i in range(10)]
    for i in range(10):
        row=list(map(int,input().split()))
        for j in range(10):
            dp[i][j]=row[j]
    
    cnt=[0]*10
    for i in range(H):
        row=list(map(int,input().split()))
        for a in row:
            if a!=-1:
                cnt[a]+=1
                
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if dp[i][k]<inf and dp[k][j]<inf:
                    dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
                    
    ans=0
    for i in range(10):
        ans+=dp[i][1]*cnt[i]
        
    print(ans)
    
                
    
    
if __name__=="__main__":
    main()
