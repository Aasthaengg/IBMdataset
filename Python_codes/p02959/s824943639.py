from collections import deque
N = int(input())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
ans = 0
tmp = A.popleft()
while A:
  b = B.popleft()
  nxt = A.popleft()
  ans += min(b, tmp + nxt)
  if b >= tmp + nxt:
    tmp = 0
  elif tmp + nxt > b >= tmp:
    tmp = tmp + nxt - b
  else:
    tmp = nxt
print(ans)