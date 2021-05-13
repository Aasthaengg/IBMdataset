import copy
ym,xm=map(int,input().split())
ym-=1
xm-=1
field=[]
for i in range(ym+1):
  field.append(list(input()))
ans=copy.deepcopy(field)
def check(x,y):
  ret=0
  chx=[0]
  chy=[0]
  if x!=0:
    chx.append(-1)
  if x!=xm:
    chx.append(1)
  if y!=0:
    chy.append(-1)
  if y!=ym:
    chy.append(1)
  for px in chx:
    for py in chy:
      if px==0 and py==0:
        continue
      if field[y+py][x+px]=="#":
        ret+=1
  return ret

for x in range(xm+1):
  for y in range(ym+1):
    if field[y][x]=="#":
      continue
    ans[y][x]=check(x,y)

for i in ans:
  for j in i:
    print(j,end="")
  print()