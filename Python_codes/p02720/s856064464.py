from collections import deque

N = int(input())

q = deque([i for i in range(1,10)])

for _ in range(N-1):
  i = q.popleft()
  if i % 10 == 0:
    q.append(i*10)
    q.append(i*10+1)
  elif i % 10 == 9:
    q.append(i*10+8)
    q.append(i*10+9)
  else:
    q.append(i*10+i%10-1)
    q.append(i*10+i%10)
    q.append(i*10+i%10+1)
    
print(q[0])