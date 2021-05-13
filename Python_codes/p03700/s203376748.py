n,a,b=map(int,input().split())
H=[0]*n
for i in range(n):
  H[i]=int(input())
ng=-1
ok=10**9+5
while ok-ng>1:
  mid=(ng+ok)//2
  c=0
  for i in range(n):
    c=c+(max(0,H[i]-b*mid+a-b-1)//(a-b))
  if c>mid:
    ng=mid
  else:
    ok=mid
print(ok)