import queue
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
q = queue.Queue()
q.put(0)
d = [-1]*n
d[0] = 0

while not q.empty():
    v = q.get()
    for i in g[v]:
        if d[i] != -1:
            continue
        d[i] = v
        q.put(i)
if -1 in d:
    print("No")
else:
    print("Yes")
    for i in d[1:]:
        print(i+1)