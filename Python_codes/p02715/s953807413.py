n,k=map(int,input().split())

bin=list(str(format(n,'b')))

mod=10**9+7
list=[0]*(k+1)
ans=0

for i in reversed(range(1,k+1)):
  p=k//i
  pn=[p]
  for x in range(len(bin)-1):
    y=pn[x]**2%mod
    pn.append(y)
  num=1
  for l in range(len(bin)):
    if bin[l]=='1':
      num=num*pn[-1-l]%mod
  j=2
  while i*j<=k:
    num=(num-list[i*j])%mod
    j=j+1
  list[i]=num
  ans=(ans+num*i)%mod
print(ans)