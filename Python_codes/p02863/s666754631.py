import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, T = map(int, input().split())

    dp = [0] * (T + 1)

    AB = []

    for k in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))

    AB.sort()
    maxdp = 0

    for i in range(N):
        a, b = AB[i]  # a:time  b:value

        dp[T] =max( maxdp + b,dp[T])
        for j in range(T - 1, a - 1, -1):
            dp[j] = max(dp[j], dp[j - a] + b)
            maxdp= max(dp[j],maxdp)
    print(dp[T])

if __name__ == "__main__":
    main()
