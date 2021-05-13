from collections import defaultdict, deque
n=int(input())
v=n*(n-1)//2
es=[[] for _ in range(v)]

for i in range(n):
    *A,=map(int,input().split())
    for j in range(n-2):
        a=A[j]
        x,y=min(a-1,i),max(a-1,i)
        ith=((n-x)+(n-1))*x//2-1+(y-x)
        b=A[j+1]
        x,y=min(b-1,i),max(b-1,i)
        jth=((n-x)+(n-1))*x//2-1+(y-x)
        es[ith].append(jth)

outs = defaultdict(list)
ins = defaultdict(int)

for v1 in range(v):
    for v2 in es[v1]:
        outs[v1].append(v2)
        ins[v2] += 1

q = deque((v1,0) for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1,cnt = q.popleft()
    res.append((v1,cnt))
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append((v2,cnt+1))
x=len(res)
if x!=v:
    print(-1)
else:
    print(res[-1][1]+1)