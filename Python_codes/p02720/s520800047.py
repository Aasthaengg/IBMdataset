from collections import deque
d=deque(list(range(1,10)))
for i in range(int(input())):
  x=d.popleft()
  r=x%10;c=x*10+r
  if r!=0:d.append(c-1)
  d.append(c)
  if r!=9:d.append(c+1)
print(x)