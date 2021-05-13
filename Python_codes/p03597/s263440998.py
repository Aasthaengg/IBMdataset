import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = int(input())

    ans = N ** 2 - A

    print(ans)


if __name__ == "__main__":
    main()
