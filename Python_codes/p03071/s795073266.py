import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, input().split())
    ans = 0
    for _ in range(2):
        if a > b:
            ans += a
            a -= 1
        else:
            ans += b
            b -= 1

    print(ans)

if __name__ == '__main__':
    main()
