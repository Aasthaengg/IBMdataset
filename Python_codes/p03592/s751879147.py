from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m,k=nii()

for i in range(n+1):
  for j in range(m+1):
    if m*i+n*j-i*j*2==k:
      print('Yes')
      exit()

print('No')