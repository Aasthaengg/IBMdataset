from collections import defaultdict,Counter
import queue

N=int(input())
ab=defaultdict(list)
for i in range(N-1):
    a,b=map(int,input().split())
    ab[a].append(b)
    ab[b].append(a)

q1=queue.Queue()
qN=queue.Queue()

dist=[None for i in range(N)]
dist[0]=1
dist[N-1]=-1

phase=1
for i in ab[1]:
    q1.put((i,phase))
for g in ab[N]:
    qN.put((g,phase))

while not (q1.empty() and qN.empty()):
    while True:
        if q1.empty():
            break
        next1,p=q1.queue[0]
        if p==phase:
            if dist[next1-1]==None:
                dist[next1-1]=1
            next1,p=q1.get()
            for i in ab[next1]:
                if dist[i-1]==None:
                    q1.put((i,phase+1))
        else:
            break


    while True:
        if qN.empty():
            break
        nextN,p=qN.queue[0]
        if p==phase:
            if dist[nextN-1]==None:
                dist[nextN-1]=-1
            nextN,p=qN.get()
            for i in ab[nextN]:
                if dist[i-1]==None:
                    qN.put((i,phase+1))
        else:
            break
    phase+=1

c=Counter(dist)
if c[-1]<c[1]:
    print("Fennec")
else:
    print("Snuke")