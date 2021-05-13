# https://atcoder.jp/contests/abc126/tasks/abc126_d

# ｄfsでやっていき、最初の点を黒か白かで固定する。偶数ならどんどん加えていく。
n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    tree[u].append((v, w))
    tree[v].append((u, w))


def dfs(tree, n):
    visited = [False] * n
    dis = [0] * n
    even = set([0])
    stack = [0]
    while stack:
        v = stack.pop()
        cur_dis = dis[v]
        for next_v, d in tree[v]:
            if not visited[next_v]:
                visited[next_v] = True
                stack.append(next_v)
                dis[next_v] = cur_dis + d
                if (cur_dis + d) % 2 == 0:
                    even.add(next_v)
    return even

even = dfs(tree, n)
for i in range(n):
    if i in even:
        print(0)
    else:
        print(1)