import itertools
x=list(input())

for lst in itertools.product(['+','-'],repeat=3):
  sum=int(x[0])
  for i in range(3):
    if lst[i]=='+':
      sum+=int(x[i+1])
    else:
      sum-=int(x[i+1])
  if sum==7:
    print(x[0]+lst[0]+x[1]+lst[1]+x[2]+lst[2]+x[3]+'=7')
    break