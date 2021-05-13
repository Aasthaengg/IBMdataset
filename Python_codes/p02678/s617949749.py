from queue import Queue
n, m = map(int, input().split())
adj = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
parents = [None] * (n+1)
parents[1] = 0
parents[0] = 0
def bfs():
    q = Queue()
    q.put(1)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if parents[v] is None:
                parents[v] = u
                q.put(v)
bfs()     
#print(parents)
if None in parents:
    print("No")
else:
    print("Yes")
    for i in range(2, n+1):
        print (parents[i])