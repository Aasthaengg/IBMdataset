import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict, deque
    n, m = map(int, readline().split())
    edge = defaultdict(list)

    for _ in range(m):
        l, r, d = map(int, readline().split())
        edge[l].append((r, d))
        edge[r].append((l, -d))

    visited = [False] * (n + 1)

    for x in range(1, n + 1):
        costs = dict()
        if not visited[x]:
            costs[x] = 0
            que = deque()
            que.append((x, 0))
            while que:
                u, cost = que.popleft()
                visited[u] = True
                while edge[u]:
                    v, w = edge[u].pop()
                    if v in costs:
                        if costs[v] != cost + w:
                            print("No")
                            sys.exit()
                    costs[v] = cost + w
                    que.append((v, cost + w))

    print("Yes")


if __name__ == '__main__':
    main()
