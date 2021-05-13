from collections import deque
N = int(input())
L = []
for _ in range(N):
  x, l = map(int, input().split())
  L.append([x-l, x+l])
L.sort(key=lambda x: x[1])
L = deque(L)
s, ans = -10**8, 0
while L:
  l = deque.popleft(L)
  if s<=l[0]:
    ans += 1
    s = l[1]
print(ans)