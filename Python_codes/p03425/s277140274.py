D={'M':0,'A':0,'R':0,'C':0,'H':0}
for k in range(int(input())):
  s=input()
  if s[0] in D.keys():
    D[s[0]]+=1

t,v=0,list(D.values())
for i in range(5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      t+=v[i]*v[j]*v[k]

print(t)
