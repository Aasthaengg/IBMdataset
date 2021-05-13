w,a,b=map(int,input().split())

if b>a+w:
  print(b-a-w)
elif b<=a+w and b>a:
  print(0)
elif b<=a and b+w>a:
  print(0)
else:
  print(a-b-w)