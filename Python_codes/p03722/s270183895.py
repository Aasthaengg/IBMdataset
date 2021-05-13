def bellman_ford(n, s, edges, init_val = float('inf')): 
    d = [init_val] * n
    d[s] = 0
    for _ in range(n):
        updated = False
        for vf, vt, w in edges:
            if d[vf] != init_val and d[vt] > d[vf] + w:
                d[vt] = d[vf] + w
                updated = True
        if not updated:
            break
    while updated: #閉路の存在
        updated = False
        for vf, vt, w in edges:
            if d[vt] > d[vf] + w:
                d[vt] = -float('inf')
                updated = True
    return d

n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b, w = map(int, input().split())
    edges.append((a-1,b-1,-w))
d = bellman_ford(n, 0, edges)
print(-d[-1] if d[-1] != -float('inf') else 'inf')
