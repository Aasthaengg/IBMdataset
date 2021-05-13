from sys import stdin
input = stdin.buffer.readline

def main():
    n = int(input())

    dp = [0, 0, 0]
    for _ in range(n):
        a, b, c = map(int, input().split())
        dp = [max(dp[1], dp[2]) + a,
            max(dp[2], dp[0]) + b,
            max(dp[0], dp[1]) + c]

    print(max(dp))

main()