import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()
    w = int(input())

    ans = S[0::w]
    print(ans)


if __name__ == "__main__":
    main()
