from itertools import groupby as g
n=int(input())
a=list(map(int,input().split()))
l=[[i,len(list(j))] for i,j in g(a)]
m=0
for i in range(len(l)):
  m+=l[i][1]//2
print(m)