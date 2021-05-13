from collections import deque

N = int(input())
line = [[] for _ in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    line[u-1].append(v-1)
    line[v-1].append(u-1)

not_visited = [-1]*N
not_visited[0] = 0
stack = deque()
stack.append(0)

while stack != deque([]):
    now = stack.popleft()
    for i in line[now]:
        if not_visited[i] == -1:
            not_visited[i] = now
            stack.append(i)

route = []
now = N-1
while not_visited[now] != 0:
    route.append(now)
    now = not_visited[now]
route.append(now)
route.reverse()

l = len(route)

not_visited = [-1]*N
for i in route[l//2:]:
    not_visited[i] = -2
not_visited[0] = 0
stack = deque()
stack.append(0)

F = 0
while stack != deque([]):
    now = stack.popleft()
    for i in line[now]:
        if not_visited[i] == -1:
            not_visited[i] = not_visited[now] + 1
            stack.append(i)
            F += 1

S = N-F-2

if F > S:
    print("Fennec")
else:
    print("Snuke")