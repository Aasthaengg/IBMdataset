from collections import deque
N = int(input())
a = list(map(int,input().split()))
d = deque()
for i in range(1,200001):
  d.append(i)
count=0
for i in a:
  if i==d[0]:
    count+=1
    d.popleft()
    
if count==0:
  print(-1)
else:
  print(N-count)