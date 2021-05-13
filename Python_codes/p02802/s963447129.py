n,m=[int(x) for x in input().split()]
Q=[0]*n
R=[0]*n
for i in range(m):
  P,s=input().split()
  p=int(P)
  if s=="AC" and Q[p-1]==0:
    Q[p-1]=1
  elif s=="WA" and Q[p-1]==0:
    R[p-1]+=1
ok=sum(Q)
for j in range(n):
  if Q[j]==0 and R[j]!=0:
    R[j]=0
bad=sum(R)
print(str(ok)+" "+str(bad))