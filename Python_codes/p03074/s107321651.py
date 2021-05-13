n,k=map(int,input().split())
s=list(input())
idx=[]
idx.append(0)
for i in range(1,n):
  if s[i]!=s[i-1]:
    idx.append(i)
arr=idx+[n]*(2*k+1)
ans=-10**18
z=0
for m in idx:
    if s[m]=='0':
      ans=max(ans,arr[z+2*k]-arr[z])
    else:
      ans=max(ans,arr[z+2*k+1]-arr[z])
    z+=1
print(ans)