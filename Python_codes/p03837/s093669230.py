## https://atcoder.jp/contests/abc051/submissions/3281251
import heapq

def dijkstra(graph, node, start):
    dist = [float("inf") for _ in range(node)]
    
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        cost, cur_node = heapq.heappop(q)
        
        if dist[cur_node] < cost:
            continue
        
        for nex_cost, nex_node in graph[cur_node]:
            dist_cand = dist[cur_node] + nex_cost
            if dist_cand < dist[nex_node]:
                dist[nex_node] = dist_cand
                heapq.heappush(q, (dist[nex_node], nex_node))

    return dist

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((c, b))
        adj[b].append((c, a))
    shortest = []
    for i in range(n):
        shortest.append(dijkstra(adj, n, i))
    ans = 0
    for i in range(n):
        for cost, j in adj[i]:
            if cost > shortest[i][j]:
                ans += 1
    print(ans // 2)
                                                                                                                                                                                                     
if __name__=='__main__':
    main()

