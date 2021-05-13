from collections import deque
n, q = map(int, input().split())
deq = deque()
for i in range(n):
    name, time = input().split(); time = int(time)
    deq.append((time, name))
ans = []
cur = 0
while deq:
    time, name = deq.popleft()
    if time <= q:
        cur += time
        ans.append("%s %d" % (name, cur))
    else:
        cur += q
        deq.append((time-q, name))
print(*ans, sep="\n")