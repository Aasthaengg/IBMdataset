import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())

    dp = [10 ** 9] * pow(2,N)
    dp[0] = 0

    for j in range(M):
        a, b = map(int, input().split())
        c = sum([pow(2, int(i) - 1) for i in input().split()])
        for i in range(pow(2,N)):
            dp[i | c] = min(dp[i | c], dp[i] + a)

    print(dp[-1] if dp[-1] !=10**9 else -1)


if __name__ == "__main__":
    main()
