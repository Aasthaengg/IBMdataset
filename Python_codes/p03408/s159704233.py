d={}
a=[]
N=int(input())
for i in range(N):
  s=input()
  if s not in a:
    a.append(s)
    d[s]=1
  else:
    d[s]+=1
  a=list(set(a))
M=int(input())
for j in range(M):
  t=input()
  if t not in a:
    a.append(t)
    d[t]=-1
  else:
    d[t]-=1
  a=list(set(a))
ans=0
for k in a:
  ans=max(ans,d[k])
print(ans)