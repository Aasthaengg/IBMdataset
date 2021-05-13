import sys


def solve(n, k, h):
    if n <= k:
        return 0
    else:
        return sum(h[: n - k])


def main():
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    h = sorted(list(map(int, input().split())))
    print(solve(n, k, h))


if __name__ == "__main__":
    main()
