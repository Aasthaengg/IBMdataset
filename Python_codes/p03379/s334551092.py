n=int(input())
import copy
l=list(map(int,input().split()))
m=copy.copy(l)
l.sort()
a=l[n//2-1]
b=l[n//2]
for i in range(n):
  if m[i]<=a:
    print(b)
  else:
    print(a)