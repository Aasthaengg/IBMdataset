from sys import stdin
def input():
    return stdin.readline()

def main():
    N, S = map(int,input().split())
    A = list(map(int,input().split()))
    mod = 998244353
    dp = [[0 for j in range(S + 1)] for i in range(N + 1)]
    dp[0][0]=1
    for i in range(1,N+1) : 
        for j in range(S + 1) : 
            if(j==0):
                dp[i][j]+=pow(2,i,mod)
            else:
                dp[i][j]+=2*dp[i-1][j]
                dp[i][j]%=mod
                if(j-A[i-1]>=0):
                    dp[i][j]+=dp[i-1][j-A[i-1]]
            dp[i][j]%=mod
    print(dp[N][S]%mod)
if __name__=="__main__":
    main()