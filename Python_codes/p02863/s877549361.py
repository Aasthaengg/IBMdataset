import sys

read = sys.stdin.buffer.read


def main():
    N, T, *AB = map(int, read().split())
    D = [(a, b) for a, b in zip(*[iter(AB)] * 2)]

    D.sort()

    dp = [0] * T
    max_sum = [0] * N
    for i, (a, b) in enumerate(D):
        for t in range(T - 1, -1, -1):
            if t >= a and dp[t] < dp[t - a] + b:
                dp[t] = dp[t - a] + b
        max_sum[i] = dp[T - 1]

    ans = 0
    for i in range(N - 1):
        if ans < max_sum[i] + D[i + 1][1]:
            ans = max_sum[i] + D[i + 1][1]

    print(ans)
    return


if __name__ == '__main__':
    main()
