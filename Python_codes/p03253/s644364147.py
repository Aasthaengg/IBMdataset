n,m=map(int,input().split())
mod=10**9+7
N=10**5+1+34
p=[1]*N #assume all are primes from start 
for i in range(2,N):
    if p[i]==1:
        for j in range(2*i,N,i):
            p[j]=0
primes=[]
for i in range(2,N):
    if p[i]==1:
        primes.append(i)

#print(primes)
fact=[1]*N
for i in range(2,N):
    fact[i]=(i*fact[i-1])%mod
ifact=[1]*N
ifact[N-1]=pow(fact[N-1],mod-2,mod)
for i in range(N-2,0,-1):
    ifact[i]=((i+1)*ifact[i+1])%mod
ans=1
#print(ifact[:10])
for x in primes:
    if x>m:
        break
    cnt=0
    #print(m,end=' before\n')
    while m%x==0:
        m//=x
        cnt+=1
    if cnt==0:
        continue
#    print(x,cnt)
    #print(m,end=' after\n')
 #   print(fact[n-1+cnt],ifact[cnt],ifact[n-1])
    val=(fact[n-1+cnt]*(ifact[cnt]*ifact[n-1])%mod)%mod
  #  print(val)
    ans=(ans*val)%mod
if m>1:
    ans=(ans*n)%mod
print(ans)
