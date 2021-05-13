from collections import defaultdict, deque

N, M = map(int, input().split())
e = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    e[u].append(v)

'''
頂点を%3で考える(1つの頂点にを3つに分解する)
(u,0)->(v,1)
(v,1)->(u,2)
(u,2)->(v,0)
'''

S, T = map(int, input().split())
q = deque([[S, 0]])
dist = [[-3]*3 for _ in range(N+1)]
dist[S][0] = 0
while q:
    u, c = q.popleft()
    for v in e[u]:
        step = (c+1) % 3
        if dist[v][step] < 0:
            dist[v][step] = c+1
            q.append([v, c+1])

print(dist[T][0]//3)