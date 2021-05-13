import sys

input = sys.stdin.readline


def main():
    N, A, B = map(int, input().split())

    ans = min(A * N, B)

    print(ans)


if __name__ == "__main__":
    main()
