n=int(input())
e=[[] for _ in range(n)]
for _ in range(n):
    u,_,*v=map(lambda x:int(x)-1, input().split())
    e[u]=sorted(v)
q=[0]
d=[-1]*n
d[0]=0
while q:
    i=q.pop(0)
    for v in e[i]:
        if d[v]==-1:
            q.append(v)
            d[v]=d[i]+1
for i in range(n):
    print(i+1,d[i])

