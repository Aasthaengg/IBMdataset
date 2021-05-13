n,m=map(int,input().split())
edge=[[]for _ in range(n)]
for _ in range(m):
  l,r,d=map(int,input().split())
  l-=1
  r-=1
  edge[l].append((r,d))
  edge[r].append((l,-d))
ans=[10**20]*n
inf=10**20
for i in range(n):
  if ans[i]!=inf:continue
  stack=[i]
  visited={i}
  ans[i]=0
  for node in stack:
    for mode,d in edge[node]:
      if ans[node]+d!=ans[mode]!=inf:exit(print("No"))
      if mode in visited:continue
      visited.add(mode)
      stack.append(mode)
      if ans[mode]==inf:
        ans[mode]=ans[node]+d
      else:
        if ans[node]+d!=ans[mode]:exit(print("No"))
print("Yes")