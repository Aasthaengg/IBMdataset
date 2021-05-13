def sieve(n=10**6):
  p=[-1]*(n+1)
  for i in a:
    if p[i]==-1:
      p[i]=1
      for j in range(2*i,n+1,i):p[j]=0
    elif p[i]==1:
      p[i]=0
  return p
n=int(input())
a=sorted(list(map(int,input().split())))
p=sieve()
ans=0
for i in a:
  ans+=p[i]
print(ans)