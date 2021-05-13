n,k=map(int,input().split())
h=[0]*n
for i in range(n):
  h[i]=int(input())
h.sort()
ans=99999999999
for i in range(n-k+1):
  ans=min(ans,abs(h[i]-h[k+i-1]))
print(ans)