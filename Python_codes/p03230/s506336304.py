import math
n = int(input())
x = (-1+math.sqrt(1+8*n))/2
if not x.is_integer():
  print ('No')
  exit (0)
x = int(x)
ans = []
k = 1
for i in range(x+1):
  a = []
  for j in range(x):
    if j >= i:
      a.append(k)
      k +=1
    else:
      a.append(ans[j][i-1])
  ans.append(a)
print ('Yes')
print (x+1)
for i in range(x+1):
  print (x,*ans[i]) 