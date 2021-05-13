from collections import deque
import math
N = int(input())
x = [0] * N
y = [0] * N
al = 1
l = 0
for i in range(N):
    al *= (i+1)
    x[i], y[i] = map(int, input().split())

que = deque()
for i in range(N):
    que.append([i])
while que:
    seq = que.popleft()
    if len(seq) == N:
        for i in range(N-1):
            l += math.sqrt((x[seq[i+1]]-x[seq[i]]) ** 2 + (y[seq[i+1]]-y[seq[i]]) ** 2)
    else:
        for i in range(N):
            if i in seq:
                continue
            seq_next = seq + [i]
            que.append(seq_next)

print(l / al)