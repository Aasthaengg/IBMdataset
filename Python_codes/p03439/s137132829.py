import sys
n=int(input())
print(0)
l=input()
L=0
if l=='Vacant':
  sys.exit()
print(n-1)
r=input()
R=n-1
if r=='Vacant':
  sys.exit()

while True:
  print((L+R)//2)
  x=input()
  X=(L+R)//2
  if x=='Vacant':
    sys.exit()
  if ((X-L)%2==1 and x==l) or ((X-L)%2==0 and x!=l):
    r=x;R=X
  else:
    l=x;L=X