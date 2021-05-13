import itertools
n=int(input())
m,a,r,c,h=0,0,0,0,0
for i in range(n):
  x=input()
  if x[0]=='M':
    m+=1
  elif x[0]=='A':
    a+=1
  elif x[0]=='R':
    r+=1
  elif x[0]=='C':
    c+=1
  elif x[0]=='H':
    h+=1
    
ans=0

for lst in itertools.combinations([m,a,r,c,h],3):
  cnt=1
  for i in lst:
    cnt*=i
    
  ans+=cnt
  
print(ans)