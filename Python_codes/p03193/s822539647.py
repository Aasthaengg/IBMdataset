import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, H, W = map(int, input().split())
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if H <= a and W <= b:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
