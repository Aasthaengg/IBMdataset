import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    import heapq
    from collections import defaultdict
    from copy import copy
    n, m = map(int, readline().split())

    used = dict()
    for i in range(n):
        used[i] = dict()

    edge = defaultdict(list)

    for i in range(m):
        a, b, c = map(int, readline().split())
        edge[a].append((b, c))
        edge[b].append((a, c))
        if a < b:
            used[a][b] = False
        else:
            used[b][a] = False

    for i in range(1,n+1):
        dist = [100000000000] * (n+1)
        dist[i] = 0
        prev = defaultdict(list)
        hq = []
        heapq.heappush(hq, (0, i))
        while hq:
            cur, u = heapq.heappop(hq)
            for v, w in edge[u]:
                if dist[v] > cur + w:
                    dist[v] = cur + w
                    prev[v] = [u]
                    heapq.heappush(hq, (cur + w, v))
                elif dist[v] == cur + w:
                    prev[v].append(u)
                    heapq.heappush(hq, (cur + w, v))

        for v, val in prev.items():
            for u in val:
                if u < v:
                    used[u][v] = True
                else:
                    used[v][u] = True

    ans = 0

    for val in used.values():
        for x in val.values():
            if not x:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
