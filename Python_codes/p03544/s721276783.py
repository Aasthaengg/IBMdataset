from collections import deque
K = int(input())
l = deque([2, 1])
for _ in range(K):
  l.append(sum(l))
  ans = l.popleft()

print(l.popleft())