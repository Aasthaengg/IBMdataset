import sys

input = sys.stdin.readline


def main():
    A, B, T = map(int, input().split())

    ans = B * (T // A)

    print(ans)


if __name__ == "__main__":
    main()
