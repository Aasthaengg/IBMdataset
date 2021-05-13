A,B,C,D,E,F=map(int,input().split())
noudo=0
water=[]
for i in range(31):
  for j in range(31):
    w=100*A*i+100*B*j
    if w<=F and w!=0:
      water.append(w)
sugar=[]
for i in range(F//C+1):
  for j in range(F//D+1):
    w=C*i+D*j
    if w<=F:
      sugar.append(w)
ans1=0
ans2=0
for i in range(len(water)):
  for j in range(len(sugar)):
    if water[i]+sugar[j]<=F:
      if sugar[j]/water[i]<=E/100:
        if noudo<sugar[j]/water[i]:
          ans1=sugar[j]+water[i]
          ans2=sugar[j]
          noudo=sugar[j]/water[i]
if ans2==0:
  print(water[0],0)
else:
  print(ans1,ans2)
