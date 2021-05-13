S=input()
n=len(S)
t=[]
for i in range(13):
  t.append(0)
t[0]=1
jkmap=[]
for j in range(10):
  jkmap.append([])
  for k in range(13):
    jkmap[j].append((10*k+j)%13)
for i in range(n):
  if S[i]=='?':
    tcopy=[0]*13
    for j in range(10):
      for k in range(13):
        tcopy[jkmap[j][k]]=(tcopy[jkmap[j][k]]+t[k])%(10**9+7)
    for j in range(13):
      t[j]=tcopy[j]
  else:
    j=int(S[i])
    tcopy=[0]*13
    for k in range(13):
      tcopy[jkmap[j][k]]=(tcopy[jkmap[j][k]]+t[k])%(10**9+7)
    for j in range(13):
      t[j]=tcopy[j]
print(t[5])
