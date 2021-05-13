a,b,k=map(int,input().split())
i=0

aa=a
bb=b
if a>=1:
  a-=k
  k-=aa
if b>=1 and k>0:
  b-=k
  k-=bb

if a<0:
  a=0
if b<0:
  b=0
print(a,b)
