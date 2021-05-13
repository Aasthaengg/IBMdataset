n=int(input())
es=[[] for _ in range(n)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    es[a-1].append((b-1,c))
    es[b-1].append((a-1,c))

q,k=map(int,input().split())
k-=1
dist=[float('inf')]*n

dist[k]=0
stack=[k]
while stack:
    now=stack.pop()
    for e,w in es[now]:
        if dist[e]==float('inf'):
            dist[e]=dist[now]+w
            stack.append(e)

for _ in range(q):
    x,y=map(int,input().split())
    x-=1
    y-=1
    print(dist[x]+dist[y])