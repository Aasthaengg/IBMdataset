n=int(input())
ans=0
arr=list(map(int,input().split()))
for i in range(1,n-1):
  nMax=max(arr[i-1],arr[i],arr[i+1])
  nMin=min(arr[i-1],arr[i],arr[i+1])
  if arr[i]!=nMax and arr[i]!=nMin:
    ans+=1
print(ans)