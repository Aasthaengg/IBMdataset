from collections import deque

n = int(input())
a = list(map(str,input().split()))
b = deque()

for i in range(n):
  if i%2== 0:
    b.append(a[i])
  else:
    b.appendleft(a[i])

if len(a)%2 == 0:
  B = ' '.join(b)
  print(B)
else:
  b.reverse()
  B = ' '.join(b)
  print(B)