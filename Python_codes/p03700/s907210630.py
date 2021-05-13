n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]

ok=10**9
ng=0

while abs(ok-ng)>1:
 mid=(ok+ng)//2

 l=[i-(mid*b) for i in h]
 cnt=0
 for j in l:
  if j<=0:
   continue
  cnt+=(j+a-b-1)//(a-b)

 if cnt<=mid:
  ok=mid
 else:
  ng=mid

print(ok)