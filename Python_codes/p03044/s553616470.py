n=int(input())
e=[[[],[]] for i in range(n)]
for i in range(n-1):
  u,v,w=map(int,input().split())
  u-=1
  v-=1
  w%=2
  e[u][w].append(v)
  e[v][w].append(u)

ans=[None for i in range(n)]
ans[0]=0
s=[0]
while s:
  ns=[]
  for i in s:
    for j in e[i][0]:
      if ans[j]!=None:
        continue
      ns.append(j)
      ans[j]=ans[i]
    for j in e[i][1]:
      if ans[j]!=None:
        continue
      ns.append(j)
      ans[j]=1-ans[i]
  s=ns
print("\n".join(map(str,ans)))