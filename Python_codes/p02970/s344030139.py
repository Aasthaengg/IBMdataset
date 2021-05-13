from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,d=nii()
num=d*2+1
print((n+num-1)//num)