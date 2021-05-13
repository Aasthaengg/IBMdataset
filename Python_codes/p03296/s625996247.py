import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    ans = 0

    for i in range(1, n):
        if a[i] == a[i - 1]:
            a[i] = 1001
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
