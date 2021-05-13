from collections import deque
N = int(input())
tmp = N
ans = deque()
while tmp != 0:
  r = tmp % 2
  ans.appendleft(r)
  tmp = (tmp-r)//(-2)
print(0 if N == 0 else "".join([str(a) for a in ans]))
