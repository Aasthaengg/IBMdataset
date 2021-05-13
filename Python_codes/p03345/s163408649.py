from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b,c,k=nii()
if k%2==0:
  print(a-b)
else:
  print(b-a)