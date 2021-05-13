import sys


def main():
    N, T, *AB = map(int, sys.stdin.buffer.read().split())
    D = [(a, b) for a, b in zip(*[iter(AB)] * 2)]

    D.sort()

    dp = [0] * T
    ans = 0

    for i, (a, b) in enumerate(D[:-1]):
        for t in range(T - 1, a - 1, -1):
            if dp[t] < dp[t - a] + b:
                dp[t] = dp[t - a] + b
        if ans < dp[T - 1] + D[i + 1][1]:
            ans = dp[T - 1] + D[i + 1][1]

    print(ans)
    return


if __name__ == '__main__':
    main()
