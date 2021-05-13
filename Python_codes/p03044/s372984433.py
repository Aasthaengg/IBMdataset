def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(2000000)


    N = int(input())
    edges = [[]for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        edges[u].append((v,w%2))
        edges[v].append((u,w%2))
    colors = [0]*(N+1)
    def dfs(n,p,c):
        colors[n] = c
        for nx,w in edges[n]:
            if nx != p:
                if w%2 == 0:
                    dfs(nx,n,c)
                else:
                    dfs(nx,n,(c+1)%2)

    dfs(1,0,0)
    for i in range(1,N+1):
        print(colors[i])

main()