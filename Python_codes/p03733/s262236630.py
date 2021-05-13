import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
# MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    n, t = map(int, input().split())
    T = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        ans += min(t, T[i+1] - T[i])
    ans += t
    print(ans)

if __name__ == '__main__':
    main()
