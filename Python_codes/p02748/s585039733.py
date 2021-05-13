A,B,M=[int(x) for x in input().rstrip().split()]
a=[int(x) for x in input().rstrip().split()]
b=[int(x) for x in input().rstrip().split()]

ans=float('inf')
for i in range(M):
  x,y,c=[int(x) for x in input().rstrip().split()]
  ans=min(ans,a[x-1]+b[y-1]-c)
mm=min(a)+min(b)
print(min(ans,mm))
