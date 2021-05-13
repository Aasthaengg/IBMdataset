w,a,b = map(int,input().split())
x = max(a,b)
y = min(a,b)
if (x-y) > w:
  print((x-y)-w)
else:
  print(0)