import sys
sys.setrecursionlimit(10**9)
MOD=10**9+7

def input():
    return sys.stdin.readline().rstrip()

def main():
    L=input()
    n=len(L)
    dp=[[0]*2 for _ in range(n+1)]
    dp[0][0]=1
    for i in range(n):
        dp[i+1][1]=dp[i][1]*3%MOD
        if L[i]=='1':
            dp[i+1][0]=dp[i][0]*2%MOD
            dp[i+1][1]+=dp[i][0]
        else:
            dp[i+1][0]=dp[i][0]
    print(sum(dp[n])%MOD)

if __name__ == '__main__':
    main()
