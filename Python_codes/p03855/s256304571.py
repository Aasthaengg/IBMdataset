import sys
from collections import Counter
input = sys.stdin.buffer.readline


def grouping(adj):
    "0-indexed の無向グラフを連結成分に分解する。"
    n = len(adj)
    ret = [-1] * n
    g = 0
    for v in range(n):
        if ret[v] == -1:
            ret[v] = g
            stack = [v]
            while stack:
                v = stack.pop()
                for nv in adj[v]:
                    if ret[nv] == -1:
                        ret[nv] = ret[v]
                        stack.append(nv)
            g += 1
    return ret


N, K, L = map(int, input().split())

pq_adj = [[] for _ in range(N)]
for _ in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    pq_adj[p].append(q)
    pq_adj[q].append(p)

rs_adj = [[] for _ in range(N)]
for _ in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    rs_adj[r].append(s)
    rs_adj[s].append(r)


group = [(g1 << 32) + g2 for g1, g2 in zip(grouping(pq_adj), grouping(rs_adj))]
c = Counter(group)
for v in range(N):
    print(c[group[v]])