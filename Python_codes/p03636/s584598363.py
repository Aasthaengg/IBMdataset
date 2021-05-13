import sys

input = sys.stdin.readline


def main():
    s = input().rstrip()

    ans = "".join([s[0], str(len(s) - 2), s[-1]])

    print(ans)


if __name__ == "__main__":
    main()
