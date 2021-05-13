import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    X, Y = [int(x) for x in input().split()]
    ans = float("inf")

    if Y - X >= 0:
        ans = min(ans, Y - X)

    if Y - -X >= 0:
        ans = min(ans, Y - -X + 1)

    if -Y - X >= 0:
        ans = min(ans, -Y - X + 1)

    if -Y - -X >= 0:
        ans = min(ans, -Y - -X + 2)

    print(ans)


if __name__ == '__main__':
    main()
