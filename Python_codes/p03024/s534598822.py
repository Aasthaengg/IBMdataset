import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    if S.count("x") >= 8:
        ans = "NO"
    else:
        ans = "YES"

    print(ans)


if __name__ == "__main__":
    main()
