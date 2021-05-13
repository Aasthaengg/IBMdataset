n,k,s=map(int,input().split())
if s==1:print(*(([1]*k)+([2]*(n-k))));exit()
if k==n:print(*[s]*n);exit()
if s%2==0:
  ans=[s//2]*(k+1)
  if s<10**8:ans+=(n-len(ans))*[10**9]
  else:ans+=(n-len(ans))*[1]
else:
  ans=[]
  for i in range(k+1):
    ans.append(s//2)
    if i%2==0:ans[-1]+=1
  if s<10**8:ans+=(n-len(ans))*[10**9]
  else:ans+=(n-len(ans))*[1]
print(*ans)