from collections import*
a=deque([1,2,3,4,5,6,7,8,9])
k=int(input())
for _ in range(k):
  i=a.popleft()
  if i%10>0:a.append(10*i+i%10-1)
  a.append(10*i+i%10)
  if i%10<9:a.append(10*i+i%10+1)
print(i)