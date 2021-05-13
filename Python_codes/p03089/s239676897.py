from collections import deque
N = int(input())
b = [int(x) - 1 for x in input().split()]
d = deque()
while b:
  popped = -1
  for i in range(len(b))[::-1]:
    if b[i] == i:
      d.appendleft(i + 1)
      popped = b.pop(i)
      break
  if popped == -1:
    print(-1)
    exit()
print(*d, sep="\n")