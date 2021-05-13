import bisect
INF=10**11
A,B,q=map(int,input().split())
a=[-INF]+[int(input()) for _ in range(A)]+[INF]
b=[-INF]+[int(input()) for _ in range(B)]+[INF]
for _ in range(q):
  x=int(input())
  i=bisect.bisect_left(a,x)
  j=bisect.bisect_left(b,x)
  ans=min(max(a[i],b[j])-x,x-min(a[i-1],b[j-1]),a[i]-b[j-1]+min(a[i]-x,x-b[j-1]),b[j]-a[i-1]+min(b[j]-x,x-a[i-1]))
  print(ans)