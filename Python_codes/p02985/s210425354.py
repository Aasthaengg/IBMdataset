from collections import deque
p = 10**9+7
N,K = map(int,input().split())
G = {i:[0,[]] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    G[a][1].append(b)
    G[b][1].append(a)
que = deque([1])
hist = [0 for _ in range(N+1)]
hist[1] = 1
A = [0 for _ in range(N+1)]
while que:
    x = que.popleft()
    for y in G[x][1]:
        if hist[y]==0:
            A[y] = 1+G[x][0]
            G[x][0] += 1
            G[y][0] += 1
            que.append(y)
            hist[y] = 1
cnt = 1
for i in range(1,N+1):
    cnt = (cnt*(K-A[i]))%p
print(cnt)