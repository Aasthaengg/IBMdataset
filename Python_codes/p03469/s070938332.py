import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    ans = "2018" + S[4:]

    print(ans)


if __name__ == "__main__":
    main()
