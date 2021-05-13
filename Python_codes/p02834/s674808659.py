import sys
input = sys.stdin.buffer.readline

from collections import deque, defaultdict

#以下０オリジンで考える

n, u, v = map(int, input().split())
u, v = u-1, v-1

G = defaultdict(lambda:deque([])) #連結リスト

#以下０オリジンで考える
for _ in range(n-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    
#start位置から繋がる全ノードへの距離を求める関数、幅優先探索
#dst_dict[player][node]がplayerとnodeの距離
def bfs(start, player):
    que = deque([(start, -1, 0)])
    while que:
        node, par, dst = que.popleft() #par:親, dst:距離
        if len(G[node]) == 1:
            dst_dict[player][node] = dst
            
        for nxt in G[node]:
            if nxt == par:
                continue
            que.append((nxt, node, dst+1))
            
dst_dict = [{}, {}]

bfs(u, 0)
bfs(v, 1)

max_time = 0
for k in dst_dict[0]:
    if dst_dict[0][k] < dst_dict[1][k]:
        max_time = max(max_time, dst_dict[1][k]-1)
    
print(max_time)
