import sys


def main():
    n = int(sys.stdin.readline())

    if n < 105:
        print(0)
        exit()

    dp = [0] * 201
    ans = 0

    for i in range(1, n + 1):
        for j in range(105, n + 1):
            if j % i == 0:
                dp[j] += 1

    for i in range(105, n + 1, 2):
        if dp[i] >= 8:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
