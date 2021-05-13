N=int(input())
Check=False
for i in range(9):
  if N%(i+1)==0 and (N/(i+1))<=9:
    Check=True
if Check==True:
  print('Yes')
else:
  print('No')