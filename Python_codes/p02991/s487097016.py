def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline
    from collections import deque
    n,m = map(int,input().split())
    Es = [[] for i in range(n)]
    Et = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        Es[a].append(b)
        Et[b].append(a)
    s,t = map(int,input().split())

    diss = [[float("INF")] for i in range(n)]
    dist = [[float("INF")] for i in range(n)]
    diss[s-1] = [0]
    dist[t-1] = [0]
    def bfs(x,E,dis):
        q = deque([])
        q.append((x,0))
        while q:
            now,d = q.popleft()
            for nex in E[now]:
                if dis[nex] == [float("INF")]:
                    dis[nex] = [d+1]
                    q.append((nex,d+1))
                else:
                    check = True
                    for i in dis[nex]:
                        if i%3 == (d+1)%3:
                            check = False
                    if check:
                        q.append((nex,d+1))
                        dis[nex].append(d+1)

    bfs(s-1,Es,diss)
    bfs(t-1,Et,dist)

    ans = float("INF")
    for i in range(n):
        for j in diss[i]:
            for k in dist[i]:
                if (j+k)%3 == 0:
                    ans = min(ans,(j+k)//3)
    if ans == float("INF"):
        print(-1)
    else:
        print(ans)
if __name__ == "__main__":
    main()
