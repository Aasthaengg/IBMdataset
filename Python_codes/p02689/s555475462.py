N,M=map(int,input().split())
*H,=map(int,input().split())

graph = [[] for _ in range(N)]
    
for _ in range(M):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

print(sum(all(H[j]<H[i]  for j in graph[i]) for i in range(N)))