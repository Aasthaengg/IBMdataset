from sys import stdin, maxsize

def main():
    input = stdin.readline

    h, n = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [maxsize] * (h + 1)
    dp[0] = 0
    for i in range(h + 1):
        for x, y in a:
            if i + x < h and dp[i + x] > dp[i] + y:
                dp[i + x] = dp[i] + y
            elif i + x >= h and dp[h] > dp[i] + y:
                dp[h] = dp[i] + y
    print(dp[h])
main()