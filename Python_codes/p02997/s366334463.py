N, K = map(int, input().split())
remaining = (N-1)*(N-2)//2 - K
if remaining < 0:
    print(-1)
    exit()
edges = []
for i in range(2, N+1):
    edges.append((1, i))
u = 2
v = 3
while remaining > 0:
    edges.append((u, v))
    v += 1
    if v == N+1:
        u += 1
        v = u + 1
    remaining -= 1
print(len(edges))
for u, v in edges:
    print(u, v)
