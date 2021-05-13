n=int(input())
A=list(map(int,input().split()))
c=1
d=0
for i in range(n-1):
  e=d+A[i+1]-A[i]
  if (d<e and d<0) or (d>e and d>0):
    c+=1
    e=0
  d=e
print(c)