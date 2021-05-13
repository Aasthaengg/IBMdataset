import sys

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    ans = 0
    for i in range(K + 1, N + 1):
        ans += (N // i) * (i - K)
        if N % i == 0:
            continue
        ans += max(0, N % i - max(K - 1, 0))
    print(ans)


if __name__ == '__main__':
    main()
