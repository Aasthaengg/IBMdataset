import sys
input=sys.stdin.readline
x,y,z,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
l1=sorted([i+j for i in a for j in b],reverse=True)[:k]
l2=sorted([i+j for i in l1 for j in c],reverse=True)[:k]
for i in l2:
  print(i)
