import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = 700 + 100 * S.count("o")

    print(ans)


if __name__ == "__main__":
    main()
