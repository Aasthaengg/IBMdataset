import bisect

n=int(input())
l=list(map(int,input().split()))

l.sort()

ans=0
for i in range(n):
  for j in range(i+1,n):
    a=l[i]
    b=l[j]
    le=bisect.bisect_left(l,max(a-b,b-a)+1)
    ri=bisect.bisect_right(l,a+b-1)
    #print(le,ri)
    f=0
    if le<=i<=ri:
      f-=1
    if le<=j<=ri:
      f-=1
    if ri-le+f>0:
      ans+=ri-le+f
    #print(a,b,ans)

print(ans//3)