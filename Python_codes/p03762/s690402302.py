import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
# INF = float("inf")


def f(l):
    ret = 0
    for k in range(len(l)):
        ret += (2 * (k + 1) - len(l) - 1) * l[k]
    return ret % MOD


def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    ans = f(x) * f(y) % MOD
    print(ans)


if __name__ == '__main__':
    main()