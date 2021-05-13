N, u, v = map(lambda x: int(x)-1, input().split())
N += 1
edges = [list(map(lambda x:int(x)-1, input().split())) for _ in range(N-1)]
adj = [[] for _ in range(N)]
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

# bfs from v
dist_from_v = [-1]*N
dist_from_v[v] = 0
Q = {v}
while Q:
    tmp = set()
    for cur in Q:
        for next in adj[cur]:
            if dist_from_v[next] == -1:
                dist_from_v[next] = dist_from_v[cur]+1
                tmp.add(next)
    Q = tmp

# bfs from u
dist_from_u = [-1]*N
dist_from_u[u] = 0
Q = {u}
while Q:
    tmp = set()
    for cur in Q:
        for next in adj[cur]:
            if dist_from_u[next] == -1:
                if dist_from_u[cur]+1 < dist_from_v[next] or True:
                    dist_from_u[next] = dist_from_u[cur]+1
                    tmp.add(next)
    Q = tmp

ans = 0
for i in range(N):
    if dist_from_u[i] < dist_from_v[i]:
        ans = max(ans, dist_from_v[i]-1)
print(ans)
exit()

dst_u = dist_from_u.index(max(dist_from_u))
dist_v_dst = dist_from_v[dst_u]
ans = dist_v_dst-1
print(ans)
