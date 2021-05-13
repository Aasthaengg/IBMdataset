import collections
n,k=map(int,input().split())
a=list(map(int,input().split()))
m=[]
m2=[0]
for i in range(n):
  m.append(a[i])
for i in range(n):
  m2.append((m2[-1]+m[i]))
for i in range(n+1):
  m2[i]-=i
  m2[i]%=k

ans=0
dict=collections.defaultdict(int)
for i in range(1,n+1):
  x=m2[i]
  if i<=k-1:
    dict[m2[i-1]]+=1
  else:
    dict[m2[i-1]]+=1
    dict[m2[i-k]]-=1
  ans+=dict[x]
print(ans)