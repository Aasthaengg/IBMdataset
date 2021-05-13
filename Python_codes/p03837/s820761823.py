import heapq
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))
vs = [[False]*n for _ in range(n)]
for i in range(n):
    ds = [-1]*n
    hq = [(0,i,None)]
    while hq:
        c,idx,v = heapq.heappop(hq)
        if ds[idx] != -1:
            if ds[idx] == c:
                vs[v[0]][v[1]] = True
            continue
        ds[idx] = c
        if v != None:
            vs[v[0]][v[1]] = True
        for j in g[idx]:
            if ds[j[0]] == -1:
                heapq.heappush(hq,(c+j[1],j[0],(idx,j[0])))
            elif ds[j[0]] == c+j[1]:
                vs[idx][j[0]] = True
res = 0
for i in range(n):
    for j in g[i]:
        if vs[i][j[0]] == False:
            res += 1
print(res//2)