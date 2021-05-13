n=int(input())
ans=10**18
for a in range(1,n):
  b=n-a
  tmp=0
  for aa in str(a):
    tmp+=int(aa)
  for bb in str(b):
    tmp+=int(bb)
  ans=min(ans,tmp)
print(ans)