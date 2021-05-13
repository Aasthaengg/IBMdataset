N,M = map(int,input().split())
INF = float("inf")
d = [INF]*N
edges = [None]*M
for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    edges[i] = (a,b,-c)
d[0] = 0
for cnt in range(N):
    update = False
    for i in range(M):
        a,b,c = edges[i]
        if d[b] > d[a]+c:
            d[b] = d[a]+c
            update = True
            if cnt == N-1 and b == N-1:
                print("inf")
                exit(0)
    if not update:
        break
print(-d[N-1])