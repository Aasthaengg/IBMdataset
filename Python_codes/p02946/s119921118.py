from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

k,x=nii()

left=max(-1000000,x-k+1)
right=min(1000000,x+k-1)

ans=[i for i in range(left,right+1)]
print(*ans)