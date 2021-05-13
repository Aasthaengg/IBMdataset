n = int(input())
G = {i:[] for i in range(1, n+1)}
for _ in range(n):
    ukv = list(map(int, input().split()))
    u = ukv[0]
    k = ukv[1]
    for i in range(2, 2+k):
        G[u].append(ukv[i])
        
stack = [1]
dist = [-1]*(n+1)
dist[1] = 0

while stack:
    target = stack.pop(0)
    for target_i in G[target]:
        if dist[target_i]==-1:
            dist[target_i] = dist[target]+1
            stack.append(target_i)
            
for i, dist_i in enumerate(dist[1:], 1):
    print(i, dist_i)
