# Depth First Search
from collections import deque

N = int(input())
nodes = []
G ={}
is_visited = {}

for _ in range(N):
    lst = list(map(int, input().split()))
    idx = lst[0]
    nodes.append(idx)
    is_visited[idx] = False
    degree = lst[1]
    if degree > 0:
        G[idx] = lst[2:]
    else:
        G[idx] = []
        
d = {}  # 最初に訪問したときの発見時刻を記録する
f = {}  # 隣接リストを調べ終えた完了時刻を記録する
t = 1

def dfs(node):
    global t
    if (is_visited[node] == True):
        return
    is_visited[node] = True
    d[node] = t
    t += 1  # 時刻を一つ進める
    # 再帰探索
    for idx in G[node]:
        dfs(idx)
    f[node] = t
    t += 1  # 関数を終了するときにも+1する


for node in nodes:  # 孤立しているノードもあるためこうして対処
    dfs(node)

for node in nodes:
    print(node, d[node], f[node])

