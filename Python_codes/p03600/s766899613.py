import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    import heapq
    n = int(readline())
    dist = [[INF] * n for _ in range(n)]
    hq = []
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        a = list(map(int, readline().split()))
        for j in range(i + 1, n):
            hq.append((a[j], i, j))
            table[i][j] = a[j]
            dist[i][j] = a[j]
            dist[j][i] = a[j]

    for i in range(n):
        dist[i][i] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    dist[j][i] = dist[i][j]

    for i in range(n):
        for j in range(i + 1, n):
            if dist[i][j] != table[i][j]:
                print(-1)
                sys.exit()

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                if k != i and k!= j:
                    if dist[i][j] == dist[i][k] + dist[k][j]:
                        break
            else:
                ans += dist[i][j]

    print(ans)


if __name__ == '__main__':
    main()
