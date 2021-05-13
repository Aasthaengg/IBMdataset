N,K=map(int,input().split())
P=[int(a)-1 for a in input().split()]
C=[int(a) for a in input().split()]
ans=-float("inf")
for si in range(N):
  x=si
  S=[]
  tot=0
  while True:
    x=P[x]
    S.append(C[x])
    tot+=C[x]
    if x==si:
      break
  L=len(S)
  t=0
  for i in range(L):
    t+=S[i]
    if i+1>K:
      break
    now=t
    if tot>0:
      e=(K-i-1)//L
      now+=tot*e
    ans=max(ans,now)
    
print(ans)