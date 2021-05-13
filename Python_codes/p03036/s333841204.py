r,d,x=map(int,input().split())

def f(i):
  if i==0:
    return x
  else:
    return r*f(i-1)-d

for i in range(10):
  print(r*f(i)-d)