import sys
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for i in range(N)]
temp = sys.stdin.readlines()
for line in temp:
    u, v, d = map(int, line.split())
    G[u-1].append([v-1, d])
    G[v-1].append([u-1, d])
    
def dfs(v, G, cur=0):
    # 色をメモ
    color[v] = cur
        
    # 隣接するノードの色を調べる
    for next_v in G[v]:
        # 隣接ノードが探索済みなら、色が正しいか確かめる
        if color[next_v[0]] != -1:
            continue
            
        # 隣接ノードが未探索なら、正しい色に更新して再帰的に探索
        if next_v[1] % 2 == 0:
            dfs(next_v[0], G, cur)
        else:
            dfs(next_v[0], G, 1-cur)

color = [-1 for i in range(N)]
dfs(0, G)
for i in range(N):
    print(color[i])