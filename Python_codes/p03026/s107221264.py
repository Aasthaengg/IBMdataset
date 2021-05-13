from collections import deque
n = int(input())
path = [[] for _ in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    path[a].append(b)
    path[b].append(a)
C = sorted(list(map(int,input().split())),reverse = True)
M = sum(C[1:])
ans = [-1]*n
que = deque([0])
i = 0
while que:
    p = que.popleft()
    ans[p] = C[i]
    i += 1
    for nxt in path[p]:
        if ans[nxt] >= 0:continue
        que.append(nxt)
print(M)
print(' '.join(str(i) for i in ans))
