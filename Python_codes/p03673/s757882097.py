from collections import deque

N = int(input())
A = [int(c) for c in input().split()]
B = deque()

is_reversed = False
for a in A:
  if is_reversed:
    B.appendleft(a)
  else:
    B.append(a)
  is_reversed = not is_reversed

if is_reversed:
  ans = map(str, reversed(B))
else:
  ans = map(str, B)

print(' '.join(ans))