n,m=map(int,input().split())
a=[0]*n
for _ in range(m):
  l,r=map(int,input().split())
  a[l-1]+=1
  a[r-1]-=1
for i in range(n-1):
  a[i+1]+=a[i]
print(['YES','NO'][any([i%2 for i in a])])