from collections import deque 
d = deque()
n, q = map(int, input().split())
for i in range(n):
    d.append(input().split())
now = 0
while d:
    name, time = d.popleft()
    time = int(time)
    if time <= q:
        now += time
        print(name, now)
    else:
        time -= q
        d.append([name, time])
        now += q