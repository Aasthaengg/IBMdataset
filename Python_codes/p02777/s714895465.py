import sys

input = sys.stdin.readline


def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input().rstrip()

    if S == U:
        ans = [A - 1, B]
    else:
        ans = [A, B - 1]

    print(*ans)


if __name__ == "__main__":
    main()
