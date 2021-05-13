from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from math import factorial

n,p=nii()
a=lnii()

x=0
y=0
for i in a:
  if i%2==0:
    x+=1
  else:
    y+=1

def solve(q):
  num=0
  while q<=y:
    num+=factorial(y)//(factorial(q)*factorial(y-q))
    q+=2
  return num

ans=2**x
if p==0:
  num=solve(0)
else:
  num=solve(1)

print(ans*num)