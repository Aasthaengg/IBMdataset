import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))

    X.sort()
    ans = float("inf")
    for l in range(N - K + 1):
        r = l + K - 1
        l2r = abs(X[l]) + abs(X[l] - X[r])
        r2l = abs(X[r]) + abs(X[r] - X[l])
        ans = min(ans, l2r, r2l)

    print(ans)


if __name__ == "__main__":
    main()
