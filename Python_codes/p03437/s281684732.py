import sys

input = sys.stdin.readline


def main():
    X, Y = map(int, input().split())

    if X % Y != 0:
        ans = X
    else:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
