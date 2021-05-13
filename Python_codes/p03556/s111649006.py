import sys

input = sys.stdin.readline


def main():
    N = int(input())

    ans = int(N ** 0.5) ** 2

    print(ans)


if __name__ == "__main__":
    main()
