import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    ans[0] = sum([a[i] * (-1) ** i for i in range(n)])
    for i in range(1, n):
        ans[i] = (a[i - 1] - ans[i - 1] // 2) * 2
    print(*ans)


if __name__ == "__main__":
    main()
