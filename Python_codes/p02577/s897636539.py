n=input()
t=len(n)
z=0
for i in range(t):
  
  z=z+int(n[i])

if z%9 ==0:
  print('Yes')
else:
  print('No')
  
