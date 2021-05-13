import sys
input = sys.stdin.readline

def main():
    MOD = 10 ** 9 + 7
    h, w = map(int, input().split())
    tizu = [input() for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if tizu[i][j] == "#":
                continue
            if i != 0:
                dp[i][j] += dp[i - 1][j]
            if j != 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD
    print(dp[-1][-1])
main()