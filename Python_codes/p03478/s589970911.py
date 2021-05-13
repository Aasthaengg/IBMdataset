import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, A, B = map(int, readline().split())
    ans = 0
    for i in range(1, N + 1):
        ns = str(i)
        s = 0
        for c in ns:
            s += int(c)
        if A <= s <= B:
            ans += i

    print(ans)


if __name__ == '__main__':
    main()
