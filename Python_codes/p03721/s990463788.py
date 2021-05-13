from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from bisect import bisect_left

n,k=nii()

l=[]
for i in range(n):
  a,b=nii()
  l.append([a,b])

l.sort(key=lambda x:x[0])

a_l=[]
b_l=[]
for a,b in l:
  a_l.append(a)
  b_l.append(b)

b_rui=[0]
for i in range(1,n+1):
  b_rui.append(b_rui[i-1]+b_l[i-1])
b_rui=b_rui[1:]

inx=bisect_left(b_rui,k)
print(a_l[inx])