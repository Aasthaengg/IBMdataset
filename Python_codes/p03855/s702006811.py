def bfs(n):
    graph = [[] for i in range(N)]

    for i in range(n):
        v, u = map(int, input().split())
        graph[v-1].append(u-1)
        graph[u-1].append(v-1)
    
    root = [i for i in range(N)]
    visited = [False] * N
    
    for i in range(N):
        if not visited[i]:
            q = graph[i]
            visited[i] = True
            
            while q:
                v = q.pop()
                root[v] = i
                visited[v] = True
                for u in graph[v]:
                    if not visited[u]:
                        visited[u] = True
                        q.append(u)
                        root[u] = i
                        
    return root

def main():
    load_root = bfs(K)
    train_root = bfs(L)
    
    count = {}
    
    city = [(i, j) for i, j in zip(load_root, train_root)]
    
    for c in city:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            
    for c in city:
        print(count[c], '', end='')

if __name__ == '__main__':
    N, K, L = map(int, input().split())
    main()