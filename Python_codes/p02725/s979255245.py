k,n=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(n):
  arr.append(k+arr[i])
ans=k
for i in range(n):
  ans=min(ans,arr[i+n-1]-arr[i])
print(ans)
