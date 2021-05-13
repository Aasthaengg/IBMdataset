from copy import copy
def prime_table(n):
  n+=1
  table=[i if i%2 else 2 for i in range(n)]
  for i in range(3,n,2):
    if table[i]==i:
      for j in range(i*i,n,2*i):
        if table[j]==j:
          table[j]=i
  return table


def prime_fact(n,table):
  p=[]
  while n!=1:
    pp=table[n]
    p.append(pp)
    n//=pp
  r={}
  for i in p:
    if i in r:
      r[i]+=1
    else:
      r[i]=1
  return r



n=int(input())
t=prime_table(10**6)
a=list(map(lambda x:prime_fact(int(x),t),input().split()))

mx=copy(a[0])
for i in a[1:]:
  for j in i:
    if j in mx:
      mx[j]=max(mx[j],i[j])
    else:
      mx[j]=i[j]


sm=0
mod=10**9+7
for i in a:
  r=1
  for j in i:
    r=(r*pow(j,i[j],mod))%mod
  sm=(sm+pow(r,mod-2,mod))%mod

  
p=1
for i in mx:
  p=(p*pow(i,mx[i],mod))%mod

print((sm*p)%mod)