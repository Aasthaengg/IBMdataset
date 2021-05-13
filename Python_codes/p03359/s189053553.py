import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, readline().split())

    ans = a - 1

    if a <= b:
        ans += 1

    print(ans)

if __name__ == '__main__':
    main()
