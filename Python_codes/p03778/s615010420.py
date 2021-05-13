W,a,b=map(int,input().split())
if b<=a<=b+W or b<=a+W<=b+W:
  print(0)
elif b>a+W:
  print(b-a-W)
else:
  print(a-b-W)