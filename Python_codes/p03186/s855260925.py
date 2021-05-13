import sys

input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())

    if A + B < C:
        ans = (A + B + 1) + B
    else:
        ans = B + C

    print(ans)


if __name__ == "__main__":
    main()
