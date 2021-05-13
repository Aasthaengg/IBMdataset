import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import permutations

    n, m, q = map(int, readline().split())
    r_ = list(map(int, readline().split()))
    r = [i-1 for i in r_]

    dist = [[10 ** 18] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, readline().split())
        a, b = a - 1, b - 1
        dist[a][b] = c
        dist[b][a] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    ans = 10 ** 18
    for per in permutations(range(q)):
        score = 0
        for i in range(q - 1):
            score += dist[r[per[i]]][r[per[i + 1]]]
        ans = min(ans, score)

    print(ans)


if __name__ == '__main__':
    main()
