import heapq
h, w = map(int, input().split())
cs = [[] for _ in range(10)]
g = [[] for _ in range(10)]
for i in range(10):
    lis = list(map(int, input().split()))
    for j in range(10):
        if i == j:
            continue
        g[j].append((i,lis[j]))
ds = [-1]*10
hq = [(0,1)]
while hq:
    c,idx = heapq.heappop(hq)
    if ds[idx] != -1:
        continue
    ds[idx] = c
    for i in g[idx]:
        if ds[i[0]] == -1:
            heapq.heappush(hq,(c+i[1],i[0]))
res = 0
for i in range(h):
    lis = list(map(int, input().split()))
    for j in lis:
        if j != 1 and j != -1:
            res += ds[j]
print(res)