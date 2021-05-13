n,x,t = [int(i) for i in input().split()]
if n%x==0:
  print(int(n/x*t))
else:
  print((int(n/x)+1)*t)