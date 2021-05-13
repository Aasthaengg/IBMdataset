N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

from collections import deque
q = deque()
q.append((0, 0))
d = [10**6]*N
d[0] = 0
while q:
    temp = q.popleft()
    v = temp[0]
    r = temp[1]
    for t in E[v]:
        if d[t] == 10**6:
            d[t] = r+1
            q.append((t, r+1))

num = N-1
for k in range((d[N-1]-1)//2):
    for v in E[num]:
        if d[v] == d[N-1]-k-1:
            num = v
            break
used = [0]*N
used[num] = 1
q = deque([0])
while q:
    temp = q.pop()
    for v in E[temp]:
        if used[v] == 0:
            used[v] = 1
            q.append(v)

if sum(used)-1 > N-sum(used)+1:
    ans = "Fennec"
else:
    ans = "Snuke"
print(ans)