N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
C = [int(c) for c in input().split()]

C.sort(reverse=True)
M = sum(C) - C[0]

from collections import deque
q = deque([0])
ans = [0]*N
ans[0] = C[0]
i = 1
while q:
    u = q.popleft()
    for v in E[u]:
        if ans[v] > 0:
            continue
        ans[v] = C[i]
        i += 1
        q.append(v)

print(M)
print(*ans)