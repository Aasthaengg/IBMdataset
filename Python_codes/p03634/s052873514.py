def main():
    n = int(input())
    G = {}
    for i in range(n):
        G[i+1] = []
    for _ in range(n-1):
        a,b,c = map(int,input().split())
        G[a] += [[b,c]]
        G[b] += [[a,c]]
    q,k = map(int,input().split())
    dist = [-1]*n
    dist[k-1] = 0
    que = [k]
    while len(que) > 0:
        s = que.pop(0)
        for [nv,c] in G[s]:
            if dist[nv-1] != -1:
                continue
            dist[nv-1] = dist[s-1]+c
            que.append(nv)
    for _ in range(q):
        x,y = map(int,input().split())
        print(dist[x-1]+dist[y-1])

if __name__ == "__main__":
    main()
