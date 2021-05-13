w,a,b = map(int,input().split())
m = b-a-w
n = a-b-w
if m>0:
  print(m)
elif n>0:
  print(n)
else:
  print(0)