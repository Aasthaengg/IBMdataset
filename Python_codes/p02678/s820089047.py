from collections import deque
N, M = map(int, input().split())
road = [[] for _ in range(N+1)]
ans = [-1]*(N+1)
d = deque()
for i in range(M):
    A, B = map(int, input().split())
    road[A].append(B)
    road[B].append(A)
d.append(1)
while len(d) != 0:
    look = d.popleft()
    for i in road[look]:
        if ans[i] == -1:
            d.append(i)
            ans[i] = look

print("Yes")
for i in range(2, N+1):
    print(ans[i])
