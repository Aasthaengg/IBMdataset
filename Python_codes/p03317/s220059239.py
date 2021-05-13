n,k=map(int,input().split())
a=list(map(int,input().split()))

l=n-k
r=k-1
if l%r==0:
  print(l//r+1)
else:
  print(l//r+2)