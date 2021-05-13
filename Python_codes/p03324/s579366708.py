import sys

input = sys.stdin.readline


def main():
    D, N = map(int, input().split())

    if N == 100:
        ans = 100 ** D * (N + 1)
    else:
        ans = 100 ** D * N

    print(ans)


if __name__ == "__main__":
    main()
