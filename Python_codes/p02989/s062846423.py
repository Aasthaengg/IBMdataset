from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
l=lnii()
l.sort()

inx=n//2-1
print(l[inx+1]-l[inx])