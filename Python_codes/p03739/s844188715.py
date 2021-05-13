n = int(input())
A = list(map(int,input().split()))

t = 0
tmp = 0
for i in range(n):
  t += A[i]  
  if i%2 == 1:
    if t >= 0:
      tmp += abs(-1-t)
      t = -1      
  else:
    if t <= 0:
      tmp += abs(1-t)
      t = 1      
  
ans = tmp

t = 0
tmp = 0
for i in range(n):
  t += A[i]  
  if i%2 == 0:
    if t >= 0:
      tmp += abs(-1-t)
      t = -1
      
  else:
    if t <= 0:
      tmp += abs(1-t)
      t = 1      
  
ans = min(ans,tmp)  
print(ans)