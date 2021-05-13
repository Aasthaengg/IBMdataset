from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

a,b=nii()
print('Yay!' if a<=8 and b<=8 else ':(')