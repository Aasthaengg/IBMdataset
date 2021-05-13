import sys
input = sys.stdin.readline

def main():
    N = int(input())
    P = list(map(float, input().split()))
    dp = [[0] * (N+1) for _ in range((N+1))]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(i+1):
            dp[i][j] = dp[i-1][j]*(1-P[i-1]) + dp[i-1][j-1]*P[i-1]
    print(sum(dp[N][N//2+1:]))

if __name__ == '__main__':
    main()