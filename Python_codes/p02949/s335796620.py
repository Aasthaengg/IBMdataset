N, M, P = map(int, input().split())
ABC = []
for _ in range(M):
    a, b, c = map(int, input().split())
    ABC.append((a, b, c))
import sys
INT_MAX = sys.maxsize # 9223372036854775807        
    
def bellman_ford(edges,num_v,source):

    dist=[INT_MAX] * num_v
    dist[source]=0

    #辺の緩和
    has_negative = False
    for i in range(num_v):
        for edge in edges:
            if edge[0] != INT_MAX and dist[edge[1]] > dist[edge[0]] + edge[2]:
                if dist[edge[0]] != INT_MAX:
                    dist[edge[1]] = dist[edge[0]] + edge[2]
                if i==num_v-1:
                    has_negative = True
    
    if has_negative == False:
        return dist
    
    negative = [False] * num_v
    for _ in range(N):
        for edge in edges:
            if dist[edge[0]] == INT_MAX:
                continue
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                negative[edge[1]] = True
            # ある頂点が負閉路の一部なら、それに隣接する頂点も負閉路の一部
            if negative[edge[0]]:
                negative[edge[1]] = True
    for i, is_negative in enumerate(negative):
        if is_negative:
            dist[i] = -1 * INT_MAX
    return dist

edges = ABC[:]
edges = [(a, b, -c+P) for a, b, c in edges]

shortest_path = bellman_ford(edges, N+1, 1)
ans = -1 * shortest_path[N]
#print(shortest_path)
if ans == -INT_MAX or ans == INT_MAX:
    print(-1)
elif ans < 0:
    print(0)
else:
    print(ans)
