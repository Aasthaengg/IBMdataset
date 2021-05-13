import sys
from collections import defaultdict


def dfs(tree, p, cnt, visited):
    visited[p] = True
    cnt_here = cnt[p]
    for c in tree.get(p):
        if visited[c]:
            continue
        cnt[c] += cnt_here
        dfs(tree, c, cnt, visited)


def main():
    input = sys.stdin.buffer.readline
    sys.setrecursionlimit(10 ** 9)
    n, q = map(int, input().split())
    tree = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    tree = dict(tree)
    cnt = [0] * (n + 1)

    for _ in range(q):
        p, x = map(int, input().split())
        cnt[p] += x
    visited = [False] * (n + 1)
    dfs(tree, 1, cnt, visited)
    print(*cnt[1:])


if __name__ == "__main__":
    main()
