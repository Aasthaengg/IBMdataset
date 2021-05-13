N,L=map(int,input().split())
b=0
ans=0
for x in range(1,N+1):
  if b==0 and abs(L+x-1)<abs(L+x):
    b=1
  else:
    ans+=L+x-1
if b==0:
  ans -= L+N-1
print(ans)
