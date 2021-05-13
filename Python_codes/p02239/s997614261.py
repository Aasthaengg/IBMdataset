import queue

n = int(input())

Graph = [[x-1 for x in list(map(int, input().split()))[2:]] for i in range(n)]


# for i in range(n):
#     li = list(map(int, input().split()))
#     a = li[0]
#     a-=1
#     b = li[2:]
#     Graph[a].append(b)


dist = [-1]*n
q = queue.Queue()

dist[0] = 0
q.put(0)

while not q.empty():
    v = q.get()

    for nv in Graph[v]:
        if dist[nv] != -1: continue

        dist[nv] = dist[v] + 1
        q.put(nv)


for v in range(n):
    print(v+1, dist[v])
