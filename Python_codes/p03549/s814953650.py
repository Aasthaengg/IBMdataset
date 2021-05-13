from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n,m=nii()

ms=1900*m+100*(n-m)
ans=ms*(2**m)

print(ans)