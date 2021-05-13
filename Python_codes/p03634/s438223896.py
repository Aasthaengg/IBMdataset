import sys
sys.setrecursionlimit(10**9)
n = int(input())
visited = [0]*n
dist = [0]*n
edge = [[] for _ in range(n)]
def dfs(k):
    visited[k]=1
    for i in edge[k]:
        if visited[i[0]]==0:
            dist[i[0]]=i[1]+dist[k]
            dfs(i[0])


    return dist
def main():

    for i in range(n-1):
        a,b,c=map(int, input().split())
        edge[a-1].append([b-1,c])
        edge[b-1].append([a-1,c])

    q,k=map(int, input().split())
    #頂点kから各頂点への距離を最初に求めておくdist[i]:頂点kから頂点iまでの距離　 dist[k]=0

    visited[k-1]=1
    dist = dfs(k-1)

    res = [0]*q
    for i in range(q):
        x,y=map(int, input().split())
        res[i]=dist[x-1]+dist[y-1]


    for i in range(q):
        print(res[i])
if __name__ == '__main__':
    main()
