n,m=map(int,input().split())
c=set(range(1,m+1))
for i in range(n):
  a=list(map(int,input().split()))
  b=set(a[1:])
  c=b&c
print(len(c))