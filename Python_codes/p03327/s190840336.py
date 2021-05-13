import sys

input = sys.stdin.readline


def main():
    N = int(input())

    if N < 1000:
        ans = "ABC"
    else:
        ans = "ABD"

    print(ans)


if __name__ == "__main__":
    main()
