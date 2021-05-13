N=input()
x=0
for idx in range(len(N)):
  x=x+int(N[idx])
if x%9==0:
  print('Yes')
else:
  print('No')