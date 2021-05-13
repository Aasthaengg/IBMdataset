A,B,C,D,E,F=map(int,input().split())

cand_water=set()
for i in range(1,30//A+1):
  for j in range(30//B+1):
    vol=i*100*A+j*100*B
    if vol<=F:
      cand_water.add(vol)
#print(cand_water)

cand_sugar=set()
if C==1 or D==1:
  cand_sugar=set(range(F+1))
else:
  for i in range(3000//C+1):
    for j in range(3000//D+1):
      vol=i*C+j*D
      if vol<=F:
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