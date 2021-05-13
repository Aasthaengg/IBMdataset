import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = [int(readline()) for _ in range(n)]

    ans = -1
    prev = -1

    for x in a:
        if prev >= x:
            ans += x
            prev = x
        elif prev + 1 == x:
            ans += 1
            prev = x
        else:
            return print(-1)

    print(ans)


if __name__ == '__main__':
    main()
