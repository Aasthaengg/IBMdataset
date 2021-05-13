import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    ans = 0

    for i in range(n):
        x, u = input().split()
        if u == "JPY":
            ans += int(x)
        else:
            ans += 380000.0 * float(x)

    print(ans)

if __name__ == '__main__':
    main()
