#ABC162-A
N=int(input())
x=N//100
y=(N-100*x)//10
z=N-100*x-10*y
if x==7 or y==7 or z==7:
  print('Yes')
else:
  print('No')