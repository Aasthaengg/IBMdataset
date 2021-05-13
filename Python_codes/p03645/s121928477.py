import queue
n,m = map(int,input().split())

adj = [[] for i in range(n)]
dist = [-1]*n
for i in range(m):
    a,b = map(int,input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
    
q = queue.Queue()
dist[0] = 0
q.put(0)

while not q.empty():
    x = q.get()
    
    for f in adj[x]:
        if dist[f] != -1:
            continue
        
        dist[f] = dist[x] + 1
        q.put(f)
     
if dist[n-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")