r,c=map(int,input().split())
N=[list(map(int,input().split())) for i in range(r)]
retu=[[0 for i in range(1)] for j in range(1)] 
for j in range(c):
  ret=0
  for i in range(r):
    ret+=N[i][j]
  if j==0:
    retu[0][0]+=ret
  else:
    retu[0].append(ret)
N.extend(retu)
for i in range(r+1):
  tuika=0
  for j in range(c):
    tuika+=N[i][j]
  N[i].append(tuika)
  
for i in range(r+1):
  for j in range(c+1):
    if j==0:
      print(N[i][j],end="")
    else:
      print("",N[i][j],end="")
  print("")
