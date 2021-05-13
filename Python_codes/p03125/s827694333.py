from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b=nii()
print(a+b if b%a==0 else b-a)