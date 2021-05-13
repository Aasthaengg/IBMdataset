N,K=map(int,input().split())
h=[0]*N
for x in range(N):
  h[x]=int(input())
h.sort()
c=1000000000
for i in range(N-K+1):
  if h[i+K-1]-h[i]<c:
    c=h[i+K-1]-h[i]
print(c)