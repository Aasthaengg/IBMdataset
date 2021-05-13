import sys
input = sys.stdin.readline

def main():
    N,M = map(int,input().split())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    MOD = 10**9+7
    
    num = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for j in range(M+1):
        dp[0][j] = 1

    ans = 1
    for i in range(N):
        for j in range(M):
            if s[i] == t[j]:
                num[i+1][j+1] = (dp[i][j])%MOD
                ans += num[i+1][j+1]
            dp[i+1][j+1] = (dp[i][j+1]+dp[i+1][j]-dp[i][j]+num[i+1][j+1])%MOD
    
    print(ans%MOD)

if __name__ == "__main__":
    main()
