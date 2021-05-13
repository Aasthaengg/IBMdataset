
min2 = lambda x,y: x if x < y else y

N = int(input())

queues = [list(map(lambda x: int(x)-1,input().split()))[::-1] for _ in range(N)]

q = set()
for i,l in enumerate(queues):
    if i < l[-1] and queues[l[-1]][-1] == i:
        q.add(i)

d = 0
while q:
    possible = set()
    for v in q:
        u = queues[v].pop()
        queues[u].pop()
        possible.add(v)
        possible.add(u)

    q.clear()
    for v in possible:
        try:
            u = queues[v][-1]
            if queues[u][-1] == v:
                q.add(min2(u,v))
        except IndexError:
            pass
    d += 1

print(-1 if any(l for l in queues) else d)