n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
  if a[i] != i + 1:
    c+=1
    
if c == 0 or c == 2:
  print('YES')
  
else:
  print('NO')

