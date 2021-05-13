from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:sorted(list(map(int,stdin.readline().split())))
from bisect import bisect_left, bisect_right

n=int(input())
a=lnii()
b=lnii()
c=lnii()

ans=0
for i in range(n):
  m=b[i]
  num1=bisect_left(a,m)
  num2=n-bisect_right(c,m)
  ans+=num1*num2

print(ans)