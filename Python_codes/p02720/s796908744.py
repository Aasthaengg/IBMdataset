from collections import deque
q=deque([1,2,3,4,5,6,7,8,9])
K=int(input())
for i in range(K-1):
  x=q.popleft()
  y=x%10
  if y>0:
    q.append(10*x+y-1)
  q.append(10*x+y)
  if y<9:
    q.append(10*x+y+1)
print(q.popleft())