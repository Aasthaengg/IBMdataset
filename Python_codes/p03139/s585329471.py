from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,a,b=nii()
print(min(a,b),max(0,a+b-n))