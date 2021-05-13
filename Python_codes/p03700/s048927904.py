import bisect
def is_ok(mid):
  ind=bisect.bisect_right(h,mid*b)
  cnt=0
  for i in range(ind,n):
    cnt+=(h[i]-mid*b+a-b-1)//(a-b)
  if cnt<=mid:return True
  else:return False
n,a,b=map(int,input().split())
h=sorted([int(input()) for _ in range(n)])
ng=-1
ok=(h[-1]+b-1)//b
while abs(ok-ng)>1:
  mid=(ok+ng)//2
  if is_ok(mid):ok=mid
  else:ng=mid
print(ok)