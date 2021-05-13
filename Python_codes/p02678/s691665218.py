from collections import deque
n,m = map(int,input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
#部屋から1までの距離(深さ)
dist = [-100 for _ in range(n)]
dist[0] = 0

#幅優先探索でdistを更新
#pに今いる位置を格納
p = deque()
p.append(0)

while len(p) > 0:
    now = p.pop()
    for i in graph[now]:
        if dist[i] != -100:
            continue
        p.appendleft(i)
        dist[i] = now
        
print('Yes')
for i in range(1,n):
    print(dist[i]+1)