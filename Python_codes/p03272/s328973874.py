import sys

input = sys.stdin.readline


def main():
    N, i = map(int, input().split())

    ans = N - i + 1

    print(ans)


if __name__ == "__main__":
    main()
