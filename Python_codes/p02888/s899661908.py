import bisect

n=int(input())
l=list(map(int,input().split()))

l.sort()
ans=0

for i in range(n-2):
  for j in range(i+1,n-1):
    a=l[i]+l[j]
    b=l[j]-l[i]
    
    x=bisect.bisect_right(l,b)
    y=bisect.bisect_left(l,a)-1
    X=max(j+1,x)
    if y-X+1>0:
      ans+=y-X+1
      
print(ans)