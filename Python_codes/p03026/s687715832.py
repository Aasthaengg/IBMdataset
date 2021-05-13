import sys
input=sys.stdin.readline
n=int(input())
Edges=[[] for _ in range(n)]
Cnt=[0]*n
for _ in range(n-1):
    a,b=map(int,input().split())
    Edges[a-1].append(b-1)
    Edges[b-1].append(a-1)
C=list(map(int,input().split()))
C.sort()
print(sum(C)-C[-1])
Used=[False]*n
Ans=[0]*n
q=[0]
Used[0]=True
while q:
    v=q.pop()
    Ans[v]=C.pop()
    for u in Edges[v]:
        if not Used[u]:
            Used[u]=True
            q.append(u)
print(*Ans)