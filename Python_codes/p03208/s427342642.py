n,k=map(int,input().split())
h=[int(input()) for i in range(n)]
h.sort()
m=10**10
for i in range(n-k+1):
  m=min(m,h[i+k-1]-h[i])
print(m)