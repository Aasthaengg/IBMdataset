from collections import deque

n, qt = map(int, input().split())
que = deque()
for i in range(n):
    name, time = input().split()
    que.append((name, int(time)))

elapsedtime = 0
while que:
    name, time = que.popleft()
    if time <= qt:
        elapsedtime += time
        print(name, elapsedtime)
    else:
        elapsedtime += qt
        time -= qt
        que.append((name, time))