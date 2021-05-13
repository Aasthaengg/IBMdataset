import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, c, k = map(int, readline().split())
    t = [int(readline()) for _ in range(n)]
    t.sort()

    ans = 0
    oldest = t[0]
    cnt = 1
    for x in t[1:]:
        if oldest + k < x or cnt == c:
            ans += 1
            cnt = 0
            oldest = x
        cnt += 1

    if cnt > 0:
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
