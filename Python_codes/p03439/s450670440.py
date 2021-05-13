import sys

N=int(input())
st=0
en=N
print(st)
sys.stdout.flush()
s=input().split()
if s=="Vacant":
  sys.exit()
a=st
b=en
c=s
d=s

for i in range(19):
  x=(a+b)//2
  print(x)
  sys.stdout.flush()
  f=input().split()

  if f=="Vacant":
    sys.exit()
  elif (x-a)%2==0 and c!=f:
    b=x
    d=f
  elif (x-a)%2==0 and c==f:
    a=x
    c=f
  elif (x-a)%2==1 and c!=f:
    a=x
    c=f
  elif (x-a)%2==1 and c==f:
    b=x
    d=f