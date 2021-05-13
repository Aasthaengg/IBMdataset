n=int(input())
arr=list(map(int,input().split()))
s=0
r=0
ans=0
for l in range(n):
  while r<n:
    if s&arr[r]!=0:
      break
    else:
      s+=arr[r]
      r+=1
  ans+=r-l
  s-=arr[l]  
print(ans)