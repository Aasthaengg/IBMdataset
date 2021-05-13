from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,a,b=nii()

min_v=a*(n-1)+b
max_v=b*(n-1)+a

print(max(0,max_v-min_v+1))