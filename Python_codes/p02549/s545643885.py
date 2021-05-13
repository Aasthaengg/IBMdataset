n,k=map(int,input().split())
l=[]
mod=998244353
for i in range(k):
  l.append(tuple(map(int,input().split())))

s=[0,1]
for i in range(1,n):
  t=0
  for j in range(k):
    t+=s[max(0,i-l[j][0]+1)]-s[max(0,i-l[j][1])]
  s.append((s[-1]+t)%mod)
print(t%mod)