from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b,c=nii()

if a%2==1 and b%2==1 and c%2==1:
  print(min(a*b,b*c,c*a))
else:
  print(0)