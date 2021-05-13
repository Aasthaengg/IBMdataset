import sys

input = sys.stdin.readline


def main():
    N = int(input())
    abc = [0] * N
    for i in range(N):
        abc[i] = list(map(int, input().split()))

    dp = [[0] * 3 for _ in range(N)]
    dp[0] = abc[0]
    for i, (a, b, c) in enumerate(abc[1:], start=1):
        dp_i = dp[i]
        dp_im = dp[i - 1]
        dp_i[0] = max(dp_im[1], dp_im[2]) + a
        dp_i[1] = max(dp_im[0], dp_im[2]) + b
        dp_i[2] = max(dp_im[0], dp_im[1]) + c

    ans = max(dp[-1])
    print(ans)


if __name__ == "__main__":
    main()
