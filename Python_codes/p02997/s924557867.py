from collections import deque
n, k = map(int, input().split())
edges = deque()

if k > (n-1)*(n-2)/2:
    print(-1)
    exit()

for i in range(1, n):
    for j in range(i+1, n+1):
        edges.append((i, j))
m = int((n-1) + (n-1)*(n-2)//2 - k)
print(m)
for i in range(m):
    edge = edges.popleft()
    print(*edge)