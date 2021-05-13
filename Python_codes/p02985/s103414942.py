n,k=map(int,input().split())
e=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(lambda x:int(x)-1,input().split())
  e[a].append(b)
  e[b].append(a)

d=[-1 for i in range(n)]
c=[0 for i in range(n)]
m=[-1 for i in range(n)]
d[0]=0
s=[0]
while s:
  ns=[]
  for i in s:
    for j in e[i]:
      if d[j]!=-1:
        continue
      ns.append(j)
      m[j]=i
      c[i]+=1
      d[j]=d[i]+1
  s=ns

mod=10**9+7
frac=[1]
for i in range(1,10**5):
  frac.append((frac[-1]*i)%mod)

r=k
for i in range(n):
  if c[i]==0:
    continue
  if d[i]==0:
    if k-1-c[i]<0:
      r=0
      break
    r=(r*frac[k-1]*pow(frac[k-1-c[i]],mod-2,mod))%mod
  else:
    if k-2-c[i]<0:
      r=0
      break
    r=(r*frac[k-2]*pow(frac[k-2-c[i]],mod-2,mod))%mod
print(r)