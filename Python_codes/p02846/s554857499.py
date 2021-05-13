t1,t2=map(int,input().split())
a,b=map(int,input().split())
c,d=map(int,input().split())
x=t1*(a-c)
y=t2*(b-d)
if x<0:
  x=-x
  y=-y
if x+y==0:
  print('infinity')
elif x+y>0:
  print(0)
else:
  print(min(1,x%abs(x+y))+2*(x//abs(x+y)))