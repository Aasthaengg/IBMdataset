n,a,b=map(int,input().split())
h=[int(input()) for i in range(n)]

h_sum=sum(h)

ok=10**9
ng=0
while abs(ok-ng)>1:
 mid=(ok+ng)//2

 l=[max(i-(mid*b),0) for i in h]
 cnt=0
 for j in l:

#  if j<=0:
#   continue

  if j%(a-b)==0:
   cnt+=j//(a-b)
  else:
   cnt+=j//(a-b)+1

 if cnt<=mid:
  ok=mid
 else:
  ng=mid

print(ok)