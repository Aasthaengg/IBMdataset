from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


n,q=map(int,readline().split())

stx=[[int(x) for x in readline().split()] for _ in range(n)]
event=[]
for s,t,x in stx:
    event.append((s-x,1,x))
    event.append((t-x,-1,x))

for i in range(q):
    event.append((int(readline()),2,i))
event.sort()

ans=[0]*q

stop=set()
hq=[]
for t,op,x in event:
    if op==1:
        heappush(hq,x)
        stop.add(x)
    elif op==-1:
        stop.remove(x)

    else:
        while hq and hq[0] not in stop:
            heappop(hq) 
        ans[x]=hq[0] if hq else -1
    
for x in ans:
    print(x)