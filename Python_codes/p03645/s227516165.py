N, M = map(int, input().split())
to = [[] for _ in range(N)]
ans = 'IMPOSSIBLE'

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    to[a].append(b)
    to[b].append(a)
    
for nxt in to[0]:
    if N - 1 in to[nxt]:
        ans = 'POSSIBLE'
        break
        
print(ans)