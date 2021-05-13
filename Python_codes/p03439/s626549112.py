import sys
N=int(input())
print(0)
s=input()
a=s
if s=='Vacant':
  sys.exit()
left=0
right=N
while True:
  n=(left+right)//2
  print(n)
  s=input()
  if s=='Vacant':
    sys.exit()
  if n%2!=0:
    if s==a:
      right=n
    else:
      left=n
  else:
    if s!=a:
      right=n
    else:
      left=n