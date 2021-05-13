from collections import deque
q = deque([1,2,3,4,5,6,7,8,9])
k = int(input())
for i in range(k-1):
  p = q.popleft()
  if p%10 != 0:
    q.append(10*p + p%10 - 1)
  q.append(10*p + p%10)
  if p%10 != 9:
    q.append(10*p + p%10 + 1)
  
    
print(q.popleft())