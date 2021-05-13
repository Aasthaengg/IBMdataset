from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
C = list(map(int, input().split()))

C.sort()
C = C[::-1]

graph = [[] for _ in range(N + 1)]
check = [1] * (N + 1)
for A, B in AB:
  graph[A].append(B)
  graph[B].append(A)

answer = [0] * (N + 1)
stack = deque()
stack.append(1)
check[1] = 0
ci = 0

while stack:
  s = stack.popleft()
  answer[s] = C[ci]
  ci += 1
  for g in graph[s]:
    if check[g]:
      check[g] = 0
      stack.append(g)
      
print(sum(C) - max(C))
print(*answer[1:])  