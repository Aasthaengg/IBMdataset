import sys
input = sys.stdin.readline

def main():
    n = int(input())
    plst = list(map(float, input().split()))
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0]= 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j - 1] * plst[i - 1] + dp[i - 1][j] * (1 - plst[i - 1])
    ans = 0
    for i in range(n // 2 + 1, n + 1):
        ans += dp[-1][i]
    print(ans)

main()