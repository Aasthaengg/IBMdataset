N,M=map(int,input().split())
P=[list(map(int,input().split())) for _ in range(M)]
for i in range(M):
  P[i].append(i)
P.sort()
j=1
k=0
for i in range(M):
  k+=1
  if P[i][0]!=j:
    j=P[i][0]
    k=1
  s=str(j)
  while len(s)!=6:
    s='0'+s
  t=str(k)
  while len(t)!=6:
    t='0'+t
  P[i].append(s+t)
P.sort(key=lambda x:x[2])
for i in range(M):
  print(P[i][3])