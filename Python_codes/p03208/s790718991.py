n, k=map(int,input().split())
a=[int(input()) for i in range(n)]
a.sort()
b=[]
for p in range(n-k+1):
  c=a[p+k-1]-a[p]
  b.append(c)
  
print(min(b))
  



