import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    if 1 + (K - 1) * 2 <= N:
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


if __name__ == "__main__":
    main()
