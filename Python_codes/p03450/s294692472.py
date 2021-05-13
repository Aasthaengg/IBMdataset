import queue
N,M=map(int,input().split())
s=[[]for i in range(N)]
for i in range(M):
    L,R,D=map(int,input().split())
    s[L-1].append((R-1,D))
    s[R-1].append((L-1,-D))

q=queue.Queue()
dist=[None]*N

for i in range(N):
    if dist[i]==None:
        dist[i]=0
        q.put(i)
    while not q.empty():
        From=q.get()
        for l in s[From]:
            To,w=l
            if dist[To]==None:
                dist[To]=dist[From]+w
                q.put(To)
            else:
                if dist[To]!=dist[From]+w:
                    print("No")
                    exit()
print("Yes")