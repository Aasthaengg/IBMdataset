from collections import defaultdict, deque
def solve():
    N = int(input())
    G = defaultdict(list)

    for i in range(N-1):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append((b,c))
        G[b].append((a,c))
    
    Q, K = map(int,input().split())
    K -= 1
    visited = [False] * N
    q = deque()
    q.append((K,0))
    visited[K] = True
    depth = [0] * N
    depth[K] = 0
    while len(q) > 0:
        now, d = q.popleft()
        for next,distance in G[now]:
            if not visited[next]:
                q.append((next,d+distance))
                visited[next] = True
                depth[next] = d+distance
        
    ans = []
    for i in range(Q):
        x,y = map(int,input().split())
        x -= 1
        y -= 1
        ans.append(depth[x] + depth[y])
    
    print(*ans,sep='\n')

if __name__ == '__main__':
    solve()