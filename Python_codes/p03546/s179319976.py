h, w = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(10)]
A = [tuple(map(int, input().split())) for _ in range(h)]
AtoOne = [1001 for i in range(10)]

from collections import deque
q = deque([[1, 0]])

while q:
    i, cost = q.popleft()
    if AtoOne[i] > cost:
        AtoOne[i] = cost
    else:
        continue

    for j in range(10):
        if i == j:
            continue
        q.append([j, cost + C[j][i]])

counts = [0] * 10
for i in range(h):
    for j in range(w):
        a = A[i][j]
        if a > -1:
            counts[a] += 1
ans = 0 
for from_i, c in enumerate(counts):
    ans += c * AtoOne[from_i]
print(ans)
