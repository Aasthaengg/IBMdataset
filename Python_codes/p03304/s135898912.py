import sys

input = sys.stdin.readline


def main():
    n, m, d = map(int, input().split())

    if d == 0:
        f = n
    else:
        f = 2 * (n - d)
    ans = (m - 1) * f / (n ** 2)

    print(ans)


if __name__ == "__main__":
    main()
