from collections import deque
n =int(input())
a = [0]+list(map(int, input().split()))
d = deque()
cnt=0
for i in range(n,0,-1):    
  for j in range(i,n+1,i):
    if a[j]==0:
      continue
    cnt+=1
  b = cnt%2
  a[i] = b
  if b == 1:
    d.appendleft(i)
  cnt = 0
print(len(d))
print(' '.join(map(str,d)))
