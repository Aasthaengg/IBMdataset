from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

n=int(input())
a=lnii()
a.sort(reverse=True)
print(sum(a[::2])-sum(a[1::2]))