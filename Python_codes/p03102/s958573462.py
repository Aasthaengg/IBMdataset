from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m,c=nii()
b=lnii()

cnt=0
for i in range(n):
  p=0
  a=lnii()
  for j in range(m):
    p+=a[j]*b[j]
  p+=c
  if p>0:
    cnt+=1

print(cnt)