from collections import deque
que=deque([i for i in range(1,10)])
k=int(input())
count=0
while count!=k:
  a=que.popleft()
  count+=1
  if a%10==9:
    que.extend([10*a+8,10*a+9])
  elif a%10==0:
    que.extend([10*a,10*a+1])
  else:
    b=a*10+(a%10)-1
    que.extend([b,b+1,b+2])
print(a)

