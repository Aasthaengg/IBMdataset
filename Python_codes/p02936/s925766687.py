N,Q = map(int,input().split())

adj = [list() for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

memo = [0]*N
for _ in range(Q):
    p,x = map(int,input().split())
    memo[p-1] += x

stack = [(None,0)]
while stack:
    p,v = stack.pop()
    for u in adj[v]:
        if u != p:
            memo[u] += memo[v]
            stack.append((v,u))

print(*memo)