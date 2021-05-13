import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    A, B = map(int, readline().split())

    ans = 0
    for i in range(A, B + 1):
        s = str(i)
        if s == s[::-1]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
