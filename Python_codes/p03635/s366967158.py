import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    ans = (n - 1) * (m - 1)
    print(ans)


if __name__ == "__main__":
    main()
