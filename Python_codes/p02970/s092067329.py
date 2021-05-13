n,d=map(int,input().split())
ans=n//(d*2+1)
if n%(d*2+1)!=0:
  ans+=1
print(ans)
