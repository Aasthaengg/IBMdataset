from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,x=nii()
a=lnii()
a.sort()

a_sum=0
for i in range(n):
  a_sum+=a[i]
  if a_sum>x:
    print(i)
    exit()

if x>sum(a):
  print(n-1)
else:
  print(n)