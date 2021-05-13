def main():    
    from collections import deque
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    e = [[] for i in range(n)]

    for i in range(m):
        a,b,c = map(int,input().split())
        a -= 1
        b -= 1
        e[a].append([b,c])
        e[b].append([a,-c])


    dis = [float("INF")]*n

    def search(x):

        q = deque([])
        dis[x] = 0
        q.append(x)
        while q:
            now = q.popleft()
            for nex,d in e[now]:
                if dis[nex] == float("INF"):
                    dis[nex] = dis[now]+d
                    q.append(nex)
                else:
                    if dis[nex] != dis[now]+d:
                        print("No")
                        exit()
            
    for i in range(n):
        if e[i] and dis[i] == float("INF"):
            search(i)
    print("Yes")

if __name__ == "__main__":
    main()