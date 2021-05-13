n,m=map(int,input().split())
k=[]
s=[]
ans=0
for i in range(m):
  kk, *ss=map(int,input().split())
  k.append(kk)
  s.append(ss)
p=list(map(int,input().split()))
for i in range(2**n):
  tmp=[]
  for j in range(n):
    if (i>>j)&1:
      tmp.append(j+1)
  for j in range(m):
    if len(set(tmp)&set(s[j])) % 2 != p[j]:
      break
  else:
    ans+=1
print(ans)