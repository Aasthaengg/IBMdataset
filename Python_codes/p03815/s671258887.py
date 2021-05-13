import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = int(readline())
    ans = 2 * (x // 11)
    if x % 11 == 0:
        pass
    elif x % 11 <= 6:
        ans += 1
    else:
        ans += 2

    print(ans)

if __name__ == '__main__':
    main()
