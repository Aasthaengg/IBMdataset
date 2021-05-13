def bfs(k):
    p=k
    frontier=[1]
    visited={1:1}
    while frontier:
        next=[]
        for u in frontier:
            if u==1:
                l=k-1
            else:
                l=k-2
            i=0
            if u in adj:
                for v in adj[u]:
                    if v not in visited:
                        visited[v]=1
                        p=(p*(l-i))%(10**9+7)
                        i+=1
                        next.append(v)
        frontier=next
    return p
  
n,k=map(int,input().split())
adj={}
for w in range(n-1):
    a,b=map(int,input().split())
    if a not in adj:
        adj[a]=[b]
    else:
        adj[a].append(b)
    if b not in adj:
        adj[b]=[a]
    else:
        adj[b].append(a)
print(bfs(k))