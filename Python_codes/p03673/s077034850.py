from collections import deque

N = int(input())
As = list(map(int,input().split()))

h = deque([])
for i in range(N):
  if i%2 == 0:
    h.append(As[i])
  else:
    h.appendleft(As[i])
    
if N%2 == 1:
  h.reverse()
  
print(" ".join(map(str,h)))