import sys
sys.setrecursionlimit(10**7)

N = int(input())
tree = [[] for _ in range(N)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    tree[a-1].append([b-1, c])
    tree[b-1].append([a-1, c])
Q, K = map(int, input().split())

dist = [-1] * N
def dfs(v, total_cost):
    # v：頂点, total_cost：今までかかったコストの合計
    dist[v] = total_cost
    for v_next, cost in tree[v]:
        if dist[v_next] >= 0:
            continue
            # v_nextが訪問済みならスキップ
        dfs(v_next, total_cost+cost)

dfs(K-1, 0)

for i in range(Q):
    x, y = map(int, input().split())
    print(dist[x-1] + dist[y-1])
