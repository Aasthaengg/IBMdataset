from collections import deque


N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
d = deque(T)
count = 0
while len(d) > 0:
    t = d.popleft() + K
    for i in range(C-1):
        if len(d) > 0 and d[0] <= t:
            d.popleft()
        else:
            break
    count += 1

print(count)
