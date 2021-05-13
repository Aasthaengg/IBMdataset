n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
import sys
if min(a)>=0:
  print(a[k-1])
  sys.exit()
if max(a)<=0:
  print((-1)*a[n-k])
  sys.exit()
  
ans=0
b=[]
for i in range(n-k+1):
  b.append(a[i+k-1]-a[i])

ans=float("INF")
for i in range(n):
  #i-k+1の正負、i+k-1の正負により変わる
  if i-k+1>=0 and i+k-1<=n-1:
    ans=min(ans,abs(a[i])+min(b[i],b[i-k+1]))
  elif i-k+1<0 and i+k-1<=n-1:
    ans=min(ans,abs(a[i])+b[i])
  elif i-k+1>=0 and i+k-1>n-1:
    ans=min(ans,abs(a[i])+b[i-k+1])
  else:
    ans=ans
    
print(ans)

    
    
    
 

