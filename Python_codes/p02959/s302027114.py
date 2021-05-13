n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
ans=0
fii=min(a[0],b[0])
ans+=fii
fii1=min(a[1],b[0]-fii)
ans+=fii1
for i in range(1,n):
  fii=min(a[i]-fii1,b[i])
  ans+=fii
  fii1=min(a[i+1],b[i]-fii)
  ans+=fii1
print(ans)