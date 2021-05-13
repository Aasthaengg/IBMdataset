import sys

input = sys.stdin.readline


def main():
    N = int(input())
    K = int(input())
    X = int(input())
    Y = int(input())

    if N <= K:
        ans = N * X
    else:
        ans = K * X + (N - K) * Y

    print(ans)


if __name__ == "__main__":
    main()
