n,m = map(int,input().split())
toi=[0 for i in range(n)]
ac=0
wa=0
for i in range(m):
  p,s=map(str,input().split())
  p=int(p)
  if s=="AC":
    if toi[p-1]!=-1:
      wa+=toi[p-1]
      ac+=1
      toi[p-1]=-1
  else:
    if toi[p-1]!=-1:
      toi[p-1]+=1
print(ac,wa)
 
