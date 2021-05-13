import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict, deque
    n, u, v = map(int, readline().split())
    edge = defaultdict(list)

    for _ in range(n - 1):
        a, b = map(int, readline().split())
        edge[a].append(b)
        edge[b].append(a)

    dist_first = defaultdict(lambda: float("INF"))
    dist_second = defaultdict(lambda: float("INF"))
    dist_first[u] = 0
    dist_second[v] = 0
    leaf = set()

    que = deque()
    que.append((v, 0))
    while que:
        cur, cost = que.popleft()
        new_cost = cost + 1
        is_leaf = True
        for nx in edge[cur]:
            if dist_second[nx] == INF:
                que.append((nx, new_cost))
                dist_second[nx] = new_cost
        if len(edge[cur]) == 1:
            leaf.add(cur)

    que.append((u, 0))
    while que:
        cur, cost = que.popleft()
        if cost < dist_second[cur]:
            new_cost = cost + 1
            for nx in edge[cur]:
                if dist_first[nx] == INF:
                    que.append((nx, new_cost))
                    dist_first[nx] = new_cost

    ans = 0
    for i in range(1, n + 1):
        if i in leaf:
            first = dist_first[i]
            second = dist_second[i]
            if first == INF:
                continue
            ans = max(ans, second - 1)

    print(ans)


if __name__ == '__main__':
    main()
