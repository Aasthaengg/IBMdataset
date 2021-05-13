import sys
input = sys.stdin.readline
n=int(input())
edge=[set() for i in range(n+1)]
for i in range(n-1):
    a,b=[int(j) for j in input().split()]
    edge[a].add(b)
    edge[b].add(a)

c=[int(j) for j in input().split()]
d=[len(i) for i in edge]

d1=[i for i,x in enumerate(d) if x==1]

ans=[None]*(n+1)
c.sort()
c.reverse()
m=sum(c)-c[0]

while d1:
    v=d1.pop()
    if not d1:
        ans[v]=c.pop()
        break
    w=edge[v].pop()
    edge[w].remove(v)
    d[w]-=1
    if d[w]==1:
        d1.append(w)
    ans[v]=c.pop()

print(m)
print(*ans[1:])

