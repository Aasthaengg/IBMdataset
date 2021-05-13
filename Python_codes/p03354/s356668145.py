from collections import deque

N,M=map(int,input().split())
p=list(map(int,input().split()))

out=[set() for i in range(N+1)]

for k in range(M):
    x,y=map(int,input().split())
    out[x].add(y)
    out[y].add(x)

rch=[False for i in range(N+1)]
ans=0
q=deque()
for i in range(1,N+1):
    if not rch[i]:
        si=set()            
        q.append(i)
        rch[i]=True
        si.add(i)
        while q:
            u=q.popleft()
            for v in out[u]:
                if not rch[v]:
                    q.append(v)
                    rch[v]=True
                    si.add(v)
        sv={p[i-1] for i in si}
        ans+=len(si&sv)
              
print(ans)