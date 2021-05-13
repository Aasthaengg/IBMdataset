x,a,b=map(int, input().split())
m=abs(x-a)
n=abs(x-b)
if m<n:
  print('A')
else:
  print('B')