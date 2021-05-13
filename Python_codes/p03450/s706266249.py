n,m=map(int,input().split())
ans=[10**10]*n
edge=[[]for _ in range(n)]
for _ in range(m):
  l,r,d=map(int,input().split())
  l-=1;r-=1
  edge[l].append((r,d))
  edge[r].append((l,-d))
for i in range(n):
  if ans[i]==10**10:
    ans[i]=0
    Q=[i]
    while Q:
      P=[]
      for j in Q:
        for k,d in edge[j]:
          if ans[k]==10**10:
            ans[k]=ans[j]+d
            P.append(k)
          elif ans[j]+d!=ans[k]:
            print("No");exit()
      Q=P
print("Yes")