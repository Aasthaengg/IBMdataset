import sys

input = sys.stdin.readline
INF = float("inf")


def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [0] * N
    for i in range(1, N):
        min_cost = INF
        for k in range(1, min(K + 1, i + 1)):
            cost = dp[i - k] + abs(h[i] - h[i - k])
            if cost < min_cost:
                min_cost = cost
        dp[i] = min_cost

    ans = dp[-1]
    print(ans)


if __name__ == "__main__":
    main()
