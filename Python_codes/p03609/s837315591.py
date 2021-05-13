import sys

input = sys.stdin.readline


def main():
    X, t = map(int, input().split())

    ans = max(0, X - t)

    print(ans)


if __name__ == "__main__":
    main()
