N, K = map(int, input().split())

if K>(N-1)*(N-2)//2:
    print(-1)
    exit()
    
edges = []

for i in range(1, N):
    edges.append((i, N))
    
cnt = 0

for i in range(1, N):
    for j in range(i+1, N):
        if cnt==(N-1)*(N-2)//2-K:
            break
        
        edges.append((i, j))
        cnt += 1

print(len(edges))

for ui, vi in edges:
    print(ui, vi)