n,m=list(map(int,input().split()))
g=[[] for _ in range(n+1)]
visited=[0]*(n+1)
x=[0]*(n+1)

for _ in range(m):
    l,r,d=list(map(int,input().split()))

    g[r].append((l,d))
    g[l].append((r,-d))

stack=list(range(1,n+1))

while len(stack)>0:
    u=stack.pop()

    visited[u]=1

    for v,d in g[u]:
        if visited[v]==1:
            continue

        x[v]=x[u]-d

        stack.append(v)

flag=True

for i in range(1,n+1):
    for j,d in g[i]:
        if x[i]-x[j]!=d:
            flag=False

if flag:
    print('Yes')
else:
    print('No')