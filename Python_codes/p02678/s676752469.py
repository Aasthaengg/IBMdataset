N, M = list(map(int, input().split()))
rooms = [list() for _ in range(N+1)]

for i in range(M):
    a, b = list(map(int, input().split()))
    rooms[a].append(b)
    rooms[b].append(a)

from collections import deque

INF = 10**9+1
steps = [INF] * (N+1)
mk = [0] * (N+1)
ck = deque([1])
steps[1] = 0

while len(ck)>0:
    i = ck.popleft()
    current = steps[i]
    for j in rooms[i]:
        if steps[j] > current+1:
            ck.append(j)
            steps[j] = current+1
            mk[j] = i

print('Yes')
for i in range(2, N+1):
    print(mk[i])
