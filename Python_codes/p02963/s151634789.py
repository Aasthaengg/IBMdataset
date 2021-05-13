s=int(input())
x1=0
y1=0
x3=1
x2=10**9
if s==10**18:
  y3=10**9
  y2=0
else:
  y3=s//(10**9)+1
  y2=10**9-s%(10**9)
a=[x1,y1,x2,y2,x3,y3]
a=map(str,a)
print((' ').join(a))