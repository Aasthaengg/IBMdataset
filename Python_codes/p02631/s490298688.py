n=int(input())
a=list(map(int,input().split()))

r1=0
for jj in range(n):
  r1=r1^a[jj]

r=[0]*n
for ii in range(n):
  r[ii]=r1^a[ii]
"""
for ii in range(n):
  print(bin(a[ii]),bin(r[ii]))
"""
print(*r)