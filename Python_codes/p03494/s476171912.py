import sys

read=sys.stdin.read
n, *a=map(int,read().split())

f=1
c=0
while f:
  for i,x in enumerate(a):
    if x%2:
      f=0
      break
    a[i]=x//2
  else:
    c+=1
print(c)
