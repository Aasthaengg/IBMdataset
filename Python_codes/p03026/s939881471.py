from collections import deque
N = int(input())
G = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
C = sorted(list(map(int,input().split())))
A = [0 for _ in range(N+1)]
hist = [0 for _ in range(N+1)]
que = deque([1])
hist[1] = 1
cur = 0
while que:
    i = que[-1]
    if len(G[i])==1:
        A[i] = C[cur]
        cur += 1
        hist[i] = 2
        que.pop()
    flag = 2
    for j in G[i]:
        if hist[j]==0:
            que.append(j)
            hist[j] = 1
            flag = 1
    if flag==2 and hist[i]==1:
        A[i] = C[cur]
        cur += 1
        hist[i] = 2
        que.pop()
cnt = 0
hist = {(i,j):0 for i in range(1,N+1) for j in G[i]}
for i in range(1,N+1):
    for j in G[i]:
        if hist[(i,j)]==0:
            cnt += min(A[i],A[j])
            hist[(i,j)] = 1
            hist[(j,i)] = 1
print(cnt)
print(*A[1:])