n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, -c))

def shortest_path(v, s, edges, inf):
    d = [inf] * v
    d[s] = 0
    for i in range(2 * n):
        update = False
        for frm, to, cost in edges:
            if d[frm] != inf and d[to] > d[frm] + cost:
                d[to] = d[frm] + cost
                update = True
        if i == n:
            memo = d[-1]
    if memo != d[-1]:
        print('inf')
        exit()
    
    return d[-1]

inf = 1e30
print(-shortest_path(n, 0, edges, inf))