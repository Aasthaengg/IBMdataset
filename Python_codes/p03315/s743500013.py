import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = S.count("+") - S.count("-")

    print(ans)


if __name__ == "__main__":
    main()
