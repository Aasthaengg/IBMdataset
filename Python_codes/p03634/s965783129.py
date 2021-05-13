n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append((b,c))
    g[b].append((a,c))
q,k = map(int,input().split())
k -= 1
c = [-1]*n
c[k] = 0
stack = [k]
while stack:
    cur = stack.pop()
    for next_,cost in g[cur]:
        if c[next_]<0:
            c[next_] = c[cur]+cost
            stack.append(next_)

for i in range(q):
    x,y = map(lambda x: int(x)-1,input().split())
    print(c[x]+c[y])