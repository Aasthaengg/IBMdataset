k,x=map(int,input().split())

l=0
r=0

if x-(k-1)<-1000000:
  l=-1000000

if x-(k-1)>=-1000000:
  l=x-(k-1)

if x+(k-1)>1000000:
  r=1000000

if x+(k-1)<=1000000:
  r=x+(k-1)

ans=list(range(l,r+1))
s=' '.join([str(n) for n in ans])
print(s)