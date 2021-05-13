A,B,C,D,E,F=map(int,input().split())

cand_water=set()
for i in range(31):
  for j in range(31):
    vol=i*100*A+j*100*B
    if 0<vol<=F:
      cand_water.add(vol)
#print(cand_water)

cand_sugar=set()
for i in range(3001):
  for j in range(3001):
    vol=i*C+j*D
    if 0<=vol<=F:
      cand_sugar.add(vol)
#print(cand_sugar)

max_concent=-1
answer=[0,0]
for water in cand_water:
  for sugar in cand_sugar:
    if water+sugar>F:
      continue
    if sugar/(water+sugar)>E/(100+E):
      continue
      
    if sugar/(water+sugar)>max_concent:
      answer=(water+sugar,sugar)
      max_concent=sugar/(water+sugar)
      
print(*answer)