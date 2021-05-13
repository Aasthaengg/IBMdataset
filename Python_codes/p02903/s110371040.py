h,w,a,b = map(int,input().split())
c = "0"*a+"1"*(w-a)
d = "1"*a+"0"*(w-a)
for _ in range(b):
  print(c)
for _ in range(h-b):
  print(d)