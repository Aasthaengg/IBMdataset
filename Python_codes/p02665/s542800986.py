n = int(input())
data = list(map(int, input().split()))

max_edge = []
for depth, a in enumerate(data):
    if depth == 0:
        edge = 1 - a
    else:
        edge = max_edge[depth-1]*2 - a
    
    if edge < 0:
        print(-1)
        exit()
    max_edge.append(edge)

ans = 0
prev_edges = 0
for idx in range(n, -1, -1):
    a = data[idx]
    cap = max_edge[idx]
    if prev_edges > 2*cap:
        print(-1)
        exit()
    edges = min(prev_edges, cap) + a
    ans += edges
    prev_edges = edges

print(ans)