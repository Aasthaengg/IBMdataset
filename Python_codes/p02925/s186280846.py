import sys
input = sys.stdin.readline
from collections import defaultdict, deque
n = int(input())
X = 10000
INF = 1 << 50
edges = defaultdict(list)
edges_r = defaultdict(list)
def topological_sort(G):

    cnt_in = defaultdict(int)
    for k in G.keys():
        for v in G[k]:
            cnt_in[v] += 1
    # print(cnt_in)
    res = []
    # 入次数==0
    q = deque([i for i in list(G.keys()) if cnt_in[i]==0])
    while len(q) > 0:
        v = q.popleft()
        res.append(v)
        for next_v in G[v]:
            # 入次数を下げていく
            cnt_in[next_v] -= 1
            # 入次数が0に残ったところを次に追加
            if cnt_in[next_v] == 0:
                q.append(next_v)
    # トポソ不可能！
    if len(G) != len(res):
        print(-1)
        exit()
    return res

for i in range(n):
    r = list(map(int, input().split()))
    # 初期
    mn = min(i, r[0]-1)
    mx = max(i, r[0]-1)
    prev = mn * n + mx
    for e in r[1:]:
        e -= 1
        mn = min(i,e)
        mx = max(i,e)
        now = mn*n+mx
        edges[prev].append(now)
        edges_r[now].append(prev)
        prev = now
vs = topological_sort(edges)

# トポソの順番で経路長を入れていく
used = [0] * n**2
# for V in vs:
#     if used[V]: continue
#     used[V] = 1
#     q = deque([V])
#     while len(q) > 0:
#         v = q.popleft()
#         for u in edges[v]: 
#             if used[u] <= used[v]:
#                 q.append(u)
#                 used[u] = max(used[u], used[v] + 1)

for V in vs:
    if used[V]:continue
    used[V] = 1
    mx = 1
    for b in edges_r[V]:
        mx = max(mx, used[b]+1)
    used[V] = mx
# print(used)
print(max(used))