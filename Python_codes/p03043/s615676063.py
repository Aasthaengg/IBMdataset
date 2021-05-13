import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    ans = 0
    for n in range(1, N + 1):
        cnt = 0
        while n < K:
            n *= 2
            cnt += 1
        ans += (1 / 2 ** cnt)

    ans /= N
    print(ans)


if __name__ == "__main__":
    main()
