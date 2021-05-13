from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().splt()))

a,b,c,d=nii()
if a+b<c+d:
  print('Right')
elif a+b==c+d:
  print('Balanced')
else:
  print('Left')