import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = list(map(int, readline().split()))

    ans = INF

    for x in A:
        cur = x
        score = 0
        while cur % 2 == 0:
            cur //= 2
            score += 1
        ans = min(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
