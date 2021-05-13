def fast_bellman_ford(n, s, graph, init_val): #どう？
    d = [init_val] * n
    d[s] = 0
    from_set = {s}
    for _ in range(n):
        next_set = set()
        for vf in from_set:
            for vt, w in graph[vf]:
                if d[vt] > d[vf] + w:
                    d[vt] = d[vf] + w
                    next_set.add(vt)
        from_set = next_set
        if not from_set:
            break
    if from_set: #閉路の存在
        while from_set:
            minus_inf = -float('inf')
            next_set = set()
            for vf in from_set:
                for vt, w in graph[vf]:
                    if d[vt] > d[vf] + w:
                        d[vt] = minus_inf
                        next_set.add(vt)
            from_set = next_set
    return d

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, -w))
d = fast_bellman_ford(n, 0, graph, float('inf'))
print(-d[-1] if d[-1] != -float('inf') else 'inf')




