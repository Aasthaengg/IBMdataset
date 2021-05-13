import sys
import collections
INF = 10**18

def dfs(s,cnt):
    visited = [False]*n
    visited[s] = True
    q = collections.deque([s])
    while q:
        p = q.pop()
        visited[p] = True
        for v in edge[p]:
            if visited[v]:
                continue
            cnt[v] += cnt[p]
            q.append(v)
    return cnt

if __name__ == "__main__":
    n,q = map(int,input().split())
    edge = [[] for i in range(n)]
    for i in range(n-1):
        a,b = map(int,input().split())
        a-=1
        b-=1
        edge[a].append(b)
        edge[b].append(a)
    cnt = [0]*n
    for i in range(q):
        v,x = map(int,input().split())
        v -= 1
        cnt[v] += x
    ans = dfs(0,cnt)
    print(*ans)
