import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a = list(map(int, readline().split()))

    ans = 0
    while all([x % 2 == 0 for x in a]):
        a[0], a[1], a[2] = a[1] + a[2], a[2] + a[0], a[0] + a[1]
        a[0] //= 2
        a[1] //= 2
        a[2] //= 2
        ans += 1
        if a[0] == a[1] == a[2]:
            return print(-1)

    print(ans)


if __name__ == '__main__':
    main()
