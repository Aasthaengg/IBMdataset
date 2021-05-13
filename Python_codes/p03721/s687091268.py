from collections import deque
N, K = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
L.sort(key = lambda x: x[0])
L = deque(L)
while K>L[0][1]:
  K -= L[0][1]
  L.popleft()
print(L[0][0])