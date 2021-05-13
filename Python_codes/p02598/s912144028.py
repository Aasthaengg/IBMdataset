n,k=map(int,input().split())
a=list(map(int,input().split()))
l,r=0,max(a)
def test(x):
  num=0
  for i in a:
    num+=i//x
    if i%x==0:
      num-=1
  if num<=k:
    return num
while r-l>1:
  mid=(l+r)//2
  if test(mid):
    r=mid
  else:
    l=mid
print(r)