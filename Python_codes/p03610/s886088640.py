import sys

input = sys.stdin.readline


def main():
    s = input().rstrip()

    ans = s[::2]

    print(ans)


if __name__ == "__main__":
    main()
