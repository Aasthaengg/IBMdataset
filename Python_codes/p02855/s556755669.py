h,w,k=map(int,input().split())
field=[list(input()) for i in range(h)]
numf=[[0 for i in range(w)] for j in range(h)]
name=0
empty=[]
for i in range(h):
  if field[i].count("#")==0:
    continue
  else:
    name+=1
    lim=field[i].count("#")+name-1
    for j in range(w):
      
      if field[i][j]==".":
        numf[i][j]=name
      elif field[i][j]=="#":
        if name==lim:
          numf[i][j]=name
        else:
          numf[i][j]=name
          name+=1
for i in range(w):
  for j in range(1,h):
    if numf[j-1][i]==0:
      continue
    else:
      if numf[j][i]==0:
        numf[j][i]=numf[j-1][i]
for i in range(w):
  for j in range(h-1)[::-1]:
    if numf[j][i]==0:
      numf[j][i]=numf[j+1][i]
for i in numf:
  print(*i)
