from heapq import*

x,y,z,K=map(int,input().split())
a=(list(map(int,input().split())))
b=(list(map(int,input().split())))
c=sorted(list(map(int,input().split())))[::-1]

d=sorted([q+p for q in a for p in b],reverse=True)[:K]

e=sorted([q+p for q in d for p in c],reverse=True)[:K]
for i in e:
  print(i)