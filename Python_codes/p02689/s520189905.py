N,M = map(int, input().split())

H=list(map(int,input().split()))

graph=[[0] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(H[B-1])
    graph[B-1].append(H[A-1])

ans=0

for i in range(N):
    if H[i]>max(graph[i]):
        ans+=1
        
print(ans)