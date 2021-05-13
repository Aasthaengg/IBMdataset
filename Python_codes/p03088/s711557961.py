import sys
input=sys.stdin.readline   
sys.setrecursionlimit(100000000)
from functools import lru_cache
INF = 1000000000
MOD = 10**9+7

def main():
    n=int(input())

    dp=[[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]

    dp[3]=[[[1]*4 for _ in range(4)] for _ in range(4)]    
    dp[3][0][2][1]=0
    dp[3][0][1][2]=0
    dp[3][2][0][1]=0
    
    cannot={(0,1,2),(0,2,1),(2,0,1)}

    for i in range(4,n+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j,k,l) in cannot:
                        dp[i][j][k][l]=0
                    else:
                        for m in range(4):
                            if (m,j,l)==(0,2,1) or (m,k,l)==(0,2,1):
                                continue
                            else:
                                dp[i][j][k][l]+=dp[i-1][m][j][k]
                                dp[i][j][k][l]%=MOD

    ans=0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans+=dp[-1][i][j][k]
                ans%=MOD
    print(ans)
if __name__=='__main__':
    main()