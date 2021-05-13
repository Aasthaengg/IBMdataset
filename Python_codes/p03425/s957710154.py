n=[input() for _ in range(int(input()))];m,a,r,c,h=0,0,0,0,0
for i in n:
  if i[0]=='M': m+=1
  elif i[0]=='A': a+=1
  elif i[0]=='R': r+=1
  elif i[0]=='C': c+=1
  elif i[0]=='H': h+=1
r=[m,a,r,c,h]
print(sum([sum([sum([r[i]*r[j]*r[k] for k in range(j+1,5)]) for j in range(i+1,5)]) for i in range(5)]))