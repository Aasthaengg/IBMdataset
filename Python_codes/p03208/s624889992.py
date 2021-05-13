n,k=map(int,input().split())
l=sorted(int(input()) for _ in range(n))
a=10**9
for i in range(n-k+1):
  a=min(a,l[i+k-1]-l[i])
print(a)