w,a,b = map(int,input().split())
if a>b:
  a,b = b,a
if a<=b and b<=a+w:
  print(0)
else:
  print(b-(a+w))