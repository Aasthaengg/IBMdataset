n,m= map(int, input().split())
ab=[]
cd=[]
for i in range(n):
  ab.append(list(map(int, input().split())))
for i in range(m):
  cd.append(list(map(int, input().split())))

for a,b in ab:
  cpt=-1
  mind=10**9
  for j in range(len(cd)):
    c,d=cd[j]
    d=abs(a-c)+abs(b-d)
    if d<mind:
      cpt=j+1
      mind=min(mind,d)
  print(cpt)