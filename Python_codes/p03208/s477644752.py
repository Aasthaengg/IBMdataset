n,k=map(int,input().split())
h=[]
for i in range(n):
  h_=int(input())
  h.append(h_)
  
h.sort()

ans=float('inf')
for i in range(1,n-k+2):
  ans=min(ans,h[n-i]-h[n-i-k+1])
  
print(ans)