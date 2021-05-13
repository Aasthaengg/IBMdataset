s=input()
an=[]
for m in "qwertyuiopasdfghjklzxcvbnm":
  i=0
  d=[len(s)-j for j in range(len(s))]
  while s.find(m,i)>=0:
    t=s.find(m,i)
    for j in range(t+1):
      d[j]=min(t-j,d[j])
    i=t+1

  mi=0
  for i in range(len(s)):
    mi=max(mi,d[i])
  an.append(max(d))
print(min(an))
