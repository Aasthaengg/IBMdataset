N = int(input())
A = list(map(int,input().split()))
x = 1
t = 0
A.sort()
for i in range(N):
  x*= A[i]
  if x>10**18:
    t = 1
    break
  
if t == 1:
  print(-1)
else:
  print(x)
  
  
