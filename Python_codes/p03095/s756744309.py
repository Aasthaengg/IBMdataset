n=int(input())
s=input()
ss=set(s)
ls={}
csp=0
for j in ss:
  ls[j]=csp
  csp+=1

iis=[]
for i in s:
  iis.append(ls[i])

mod=10**9+7
d=[0 for i in range(csp)]
for i in iis:
  d[i]+=1
c=1
for i in d:
  c=(c*(i+1))%mod

print((c+mod-1)%mod)