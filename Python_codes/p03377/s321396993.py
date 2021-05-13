import sys

input = sys.stdin.readline


def main():
    A, B, X = map(int, input().split())

    if A <= X <= A + B:
        ans = "YES"
    else:
        ans = "NO"

    print(ans)


if __name__ == "__main__":
    main()
