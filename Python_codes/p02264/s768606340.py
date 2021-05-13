from collections import deque

n, q = map(int, input().split())
dq = deque()
for _ in range(n):
    p, t = map(str, input().split())
    dq.append([p, int(t)])
total = 0
while dq:
    pt = dq.popleft()
    if pt[1] <= q:
        total += pt[1]
        print(pt[0], total)
    else:
        total += q
        dq.append([pt[0], pt[1]-q])