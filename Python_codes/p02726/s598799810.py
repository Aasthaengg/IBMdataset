import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def bfs(root):
        dist = [f_inf] * n
        dist[root] = 0
        que = deque()
        que.append(root)
        while que:
            prev = que.popleft()
            for next in tree[prev]:
                if dist[next] == f_inf:
                    dist[next] = dist[prev] + 1
                    que.append(next)
        return dist

    n, x, y = map(int, input().split())
    tree = [[] for _ in range(n)]
    for i in range(n - 1):
        tree[i].append(i + 1)
        tree[i + 1].append(i)
    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)

    cnt = [0] * n
    for i in range(n):
        dist = bfs(i)
        for d in dist:
            cnt[d] += 1

    for i in range(1, n):
        print(cnt[i] // 2)


if __name__ == '__main__':
    resolve()
