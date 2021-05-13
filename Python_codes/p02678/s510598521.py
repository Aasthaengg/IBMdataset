import queue
import sys
imput = sys.stdin.readline

n,m = map(int,input().split()) 

conne = [[] for _ in range(n+1)]
dist = [99999]*(n+1)
par = [0] * (n+1)

for i in range(m):
    a,b = map(int,input().split()) 
    conne[a].append(b)
    conne[b].append(a)
    
q=queue.Queue()
dist[1] = 0
q.put((1,0))

while not q.empty():
    
    x,d = q.get()
    
    for i in conne[x]:
        if dist[i]==99999:
            q.put((i,d+1))
            par[i] = x
            dist[i] = d+1


print("Yes")    

for i in par[2:]:
    print(i)

