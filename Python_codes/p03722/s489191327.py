from collections import deque

def fast_bellman_ford(n, s, graph, edge_n, init_val): #どう？
    d = [init_val] * n
    d[s] = 0
    q = deque([s])
    checker = [-1] * n
    for i in range(n):
        m = len(q)
        for _ in range(m):
            vf = q.popleft()
            for vt, w in graph[vf]:
                if d[vt] > d[vf] + w:
                    d[vt] = d[vf] + w
                    if checker[vt] < i:
                        q.append(vt)
                        checker[vt] = i
        if not q:
            break
    if q: #閉路の存在
        minus_inf = -float('inf')
        i += 1
        while q:
            m = len(q)
            for _ in range(m):
                vf = q.popleft()
                for vt, w in graph[vf]:
                    if d[vt] > d[vf] + w:
                        d[vt] = minus_inf
                        if checker[vt] < i:
                            q.append(vt)
                            checker[vt] = i
            i += 1
    return d

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, w = map(int, input().split())
    graph[a-1].append((b-1, -w))
d = fast_bellman_ford(n, 0, graph, 2 * m, float('inf'))
print(-d[-1] if d[-1] != -float('inf') else 'inf')




