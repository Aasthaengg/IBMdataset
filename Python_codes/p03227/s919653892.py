import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    if len(S) == 2:
        ans = S
    else:
        ans = S[::-1]

    print(ans)


if __name__ == "__main__":
    main()
