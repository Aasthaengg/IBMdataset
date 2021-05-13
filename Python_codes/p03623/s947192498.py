from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

x,a,b=nii()
print('A' if abs(x-a)<abs(x-b) else 'B')