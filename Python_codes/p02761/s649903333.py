a,b=map(int,input().split())
c2=10**a
if(a==1):c1=0
else:c1=c2//10
v = [-1]*b
for i in range(b):
  n,m=map(int,input().split())
  v[i] = [n,m]
#print(v) 

for i in range(c1,c2):
  p =str(i)
  t=True
  for j in v:
    
    if(int(p[j[0]-1]) != j[1]):
      t=False
      break
  
  if(t):print(i);exit()
  
print(-1)