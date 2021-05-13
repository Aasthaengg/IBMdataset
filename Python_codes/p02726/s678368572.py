import heapq

def dijkstra(s):  #スタート
    hq = [(0, s)]  #(距離,地点)
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost


n,x,y=map(int,input().split())
e=[[] for i in range(n)]
for i in range(1,n):
  a,b=i,i+1
  e[a-1].append((1,b-1))
  e[b-1].append((1,a-1))

e[x-1].append((1,y-1))
e[y-1].append((1,x-1))

ans=[0]*(n-1)

for i in range(n):
  xxx=dijkstra(i)
  for j in xxx:
    ans[j-1]+=1

ans[-1]=0

for i in ans:
  print(i//2)