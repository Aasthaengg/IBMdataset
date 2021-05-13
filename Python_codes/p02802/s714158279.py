def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
ans,pena=0,0
N,M=MI()
P=[0]*N
PENA=[0]*N
for i in range(M):
  p,s=input().split()
  p=int(p)
  p-=1
  if s=='AC':
    if P[p]==0:
      ans+=1
      P[p]=1
      if PENA[p]!=0:
        pena+=PENA[p]
  if s=='WA':
    if P[p]==0:
      PENA[p]+=1
print(ans,pena)
