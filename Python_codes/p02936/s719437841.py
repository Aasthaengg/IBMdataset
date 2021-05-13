N,Q=map(int,input().split())
A=[[]for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    A[a].append(b)
    A[b].append(a)
B=[0]*(N+1)
for _ in range(Q):
    p,x=map(int,input().split())
    B[p]+=x

from collections import deque

dist=[-1]*(N+1) # 出力に合わせて適宜変更
dist[0]=0
dist[1]=0

D=deque()
D.append(1)

while D:
    V=D.popleft()
    for i in A[V]:
        if dist[i]!=-1:
            continue
        dist[i]=0
        B[i]+=B[V] # 出力に合わせて適宜変更（答えに直結するので最重要）
        D.append(i)

print(*B[1:])