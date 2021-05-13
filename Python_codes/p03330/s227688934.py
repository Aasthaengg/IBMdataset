n,c=map(int,input().split())
d=[]
for i in range(c):
  d.append(list(map(int,input().split())))
col=[]
for i in range(n):
  col.append(list(map(int,input().split())))
lc1=[]
lc2=[]
lc3=[]
for i in range(c):
  ccount1=0
  ccount2=0
  ccount3=0
  for j in range(n):
    for k in range(n):
      if (j+k)%3==0:
        ccount1+=d[col[j][k]-1][i]
      elif (j+k)%3==1:
        ccount2+=d[col[j][k]-1][i]
      else:
        ccount3+=d[col[j][k]-1][i]
  lc1.append(ccount1)
  lc2.append(ccount2)
  lc3.append(ccount3)
min=10**10
for i in range(c):
  for j in range(c):
    for k in range(c):
      if i==j or j==k or i==k:
        pass
      else:
        if min>lc1[i]+lc2[j]+lc3[k]:
          min=lc1[i]+lc2[j]+lc3[k]
print(min)
