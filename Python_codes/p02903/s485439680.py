h,w,a,b=map(int,input().split())
x=''
y=''
for i in range(a):
  x+='1'
  y+='0'
for i in range(w-a):
  x+='0'
  y+='1'
for i in range(b):
  print(x)
for i in range(h-b):
  print(y)