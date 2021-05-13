from collections import deque

N,M=map(int,input().split())
a=[[[] for j in range(N)] for i in range(3)] # 0-indexのグラフが3つある
for i in range(M):
    u,v=map(lambda x:int(x)-1,input().split())
    a[0][u].append((1,v))
    a[1][u].append((2,v))
    a[2][u].append((0,v))
S,T=map(lambda x:int(x)-1,input().split())
# print(a)

r=[[-3 for j in range(N)] for i in range(3)]
q=deque()
q.append((0,S));r[0][S]=0
while q:
    ui,uj=q.popleft()
    for vi,vj in a[ui][uj]:
        if r[vi][vj]==-3:
            r[vi][vj]=r[ui][uj]+1
            q.append((vi,vj))
# print(r)
print(r[0][T]//3)