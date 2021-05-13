import sys
n=int(input())
a=[-1]*n
print(0)
sys.stdout.flush()
a[0]=input()
l=0
print(n-1)
sys.stdout.flush()
r=n-1
a[n-1]=input()
while l!=r:
  if r==l+1:
    try1=r
  else:
    try1=(l+r)//2
  print(try1)
  sys.stdout.flush()
  a[try1]=input()
  if a[try1]=='Vacant':
    sys.exit()
  if ((r-try1)%2==0 and a[try1]!=a[r]) or ((r-try1)%2==1 and a[try1]==a[r]):
    l=try1
  else:
    r=try1
