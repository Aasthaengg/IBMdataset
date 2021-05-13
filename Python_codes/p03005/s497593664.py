import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())

    if K == 1:
        ans = 0
    else:
        ans = N - K

    print(ans)


if __name__ == "__main__":
    main()
