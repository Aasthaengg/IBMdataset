import sys

input = sys.stdin.readline
P = 10**9 + 7


def main():
    N, M = map(int, input().split())

    if abs(N - M) > 1:
        ans = 0
    else:
        n = 1
        for i in range(1, N + 1):
            n = (n * i) % P
        m = 1
        for i in range(1, M + 1):
            m = (m * i) % P

        ans = (n * m) % P
        if N == M:
            ans = (2 * ans) % P

    print(ans)


if __name__ == "__main__":
    main()
