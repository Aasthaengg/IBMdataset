n = int(input())
a = n//4
b = n//7
ans = False

for i in range(a+1):
  for j in range(b+1):
    if i*4+j*7 == n:
      ans = True

if ans == True:
  print('Yes')
else:
  print('No')