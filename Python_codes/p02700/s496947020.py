from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b,c,d=nii()

i=0
while a>0 and c>0:
  if i%2==0:
    c-=b
  else:
    a-=d
  i+=1

print('Yes' if a>0 else 'No')