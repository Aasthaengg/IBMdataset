A,B,C,D,E,F=map(int,input().split())
mizu=[0]*31
mizu[0]=1
satou=[0]*1501
satou[0]=1
noudo=0
for i in range(31):
 if i>=A:
  mizu[i]+=mizu[i-A]
 if i>=B:
  mizu[i]+=mizu[i-B]
for i in range(1501):
 if i>=C:
  satou[i]+=satou[i-C]
 if i>=D:
  satou[i]+=satou[i-D]
for i in range(31):
 for j in range(1501):
  if mizu[i]>0 and satou[j]>0 and (i+j)>0:
   if  j<=E*i and 100*i+j<=F and 100*j/(i+j)>=noudo:
    noudo=100*j/(i+j)
    ans=[100*i+j,j]
print(*ans)