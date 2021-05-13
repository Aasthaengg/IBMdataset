import sys
t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
n1=(b1-a1)*t1
n2=(b2-a2)*t2
if n1*n2>0 or abs(n1)>abs(n2):
  print(0)
  sys.exit()
if abs(n1)==abs(n2):
  print('infinity')
  sys.exit()
c=abs(n1)//abs(n1+n2)
while (c+1)*abs(n1+n2)<=abs(n1):
  c+=1
ans=2*c
if abs(n1)%(abs(n1+n2))!=0:
  ans+=1
print(ans)
