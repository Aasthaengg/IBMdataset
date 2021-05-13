n,k=map(int,input().split())
a=list(map(int,input().split()))
f=list(map(int,input().split()))
a.sort()
f.sort(reverse=True)

def check(s):
  ret=0
  for i,j in zip(a,f):
    ret+=max(0,i-s//j)
  return ret<=k

ok=10**12+1
ng=-1
while ok-ng>1:
  mid=(ok+ng)//2
  if check(mid):
    ok=mid
  else:
    ng=mid
print(ok)