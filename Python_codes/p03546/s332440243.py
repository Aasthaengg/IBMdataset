import heapq

H,W = map(int,input().split())
edges = [{}for _ in range(10)]
for i in range(10):
    l = list(map(int,input().split()))
    for j in range(10):
        if j != i:
            edges[j][i] = l[j]
costDic = {}
que = [(0,1)]
heapq.heapify(que)
while que:
    cost,now = heapq.heappop(que)
    if now not in costDic:
        costDic[now] = cost
        for nx,c in edges[now].items():
            if nx not in costDic:
                heapq.heappush(que,(cost+c,nx))

ans = 0
for i in range(H):
    wall = list(map(int,input().split()))
    for j in range(W):
        n = wall[j]
        if n != -1:
            ans += costDic[n]

print(ans)
