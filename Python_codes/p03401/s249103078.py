import copy
n=int(input())
a=[int(x) for x in input().rstrip().split()]
aa=copy.deepcopy(a)
a=[0]+a+[0]
sa=[]
for i in range(n+1):
  sa.append(abs(a[i+1]-a[i]))

SUM=sum(sa)
for i in range(1,n+1):
  print(SUM-(sa[i-1]+sa[i])+abs(a[i-1]-a[i+1]))