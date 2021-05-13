from collections import deque
N = int(input())
G = [[] for i in range(N)]
D = [0]*N
for i in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
    D[a-1] += 1
    D[b-1] += 1
*C, = map(int, input().split())
C.sort()

U = [1]*N
que = deque()
for i in range(N):
    if D[i] <= 1:
        que.append(i)
        U[i] = 0
it = iter(C).__next__
ans = [0]*N
R = 0
while que:
    v = que.popleft()
    ans[v] = r = it()
    R += r
    for w in G[v]:
        if U[w] == 0:
            continue
        D[w] -= 1
        if D[w] <= 1:
            U[w] = 0
            que.append(w)
print(R - C[-1])
print(*ans)