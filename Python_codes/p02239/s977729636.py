from collections import deque
N = int(input())
#グラフ入力受取
G = [[] for _ in range(N)]
for _ in range(N):
    a = list(map(int, input().split()))
    for i in a[2:]:
        G[a[0]-1].append(i-1)

#頂点1をスタートとした探索
dist = [-1]*N
que = deque()
dist[0] = 0
que.append(0)
while len(que)!=0:
    v = que.popleft()
    for nv in G[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v]+1
            que.append(nv)
        
for i in range(N):
    print(str(i+1) + ' ' + str(dist[i]))
