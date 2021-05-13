import sys
input=sys.stdin.readline   
sys.setrecursionlimit(100000000)
from functools import lru_cache
INF = 1000000000
MOD = 10**9+7

def main():
    n=int(input())
    s=input()

    dp=[[0]*(1+n) for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1,n):
            if s[i]==s[j]:
                dp[i+1][j+1]=min(dp[i][j]+1,j-i)          
    
    ans=0
    for i in range(n+1):
        for j in range(i+1,n+1):
            ans=max(ans,dp[i][j])
    print(ans)

if __name__=='__main__':
    main()