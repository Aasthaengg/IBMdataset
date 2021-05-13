def BFS(G):
    ans = [0] + [[i+1,-1] for i in range(len(G))]
    def main(G,i,d):
        if -1 < ans[i][1] <= d: return
        ans[i] = [i, d]
        for j in G[i-1][2:]: main(G,j,d+1)
    main(G,1,0)
    return ans[1:]


if __name__=='__main__':
    n = int(input())
    G = [list(map(int,input().split())) for _ in range(n)]
    for out in BFS(G): print(*out)