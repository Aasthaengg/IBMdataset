n,k=list(map(int,input().split()))
h=[]
for i in range(n):
  h.append(int(input()))
h.sort()
ans=max(h)
for i in range(n-k+1):
  ans=min(ans,h[i+k-1]-h[i])
print(ans)
