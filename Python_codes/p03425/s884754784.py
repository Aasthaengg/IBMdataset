import sys

n=int(input())
if n<3:
  print(0)
  sys.exit()

m,a,r,c,h = 0,0,0,0,0

for i in range(n):
  s=input()
  s0=s[0]
  
  if s0=="M":
    m+=1
  elif s0=="A":
    a+=1
  elif s0=="R":
    r+=1
  elif s0=="C":
    c+=1
  elif s0=="H":
    h+=1

l=[m,a,r,c,h]


ans=0
for i in range(len(l)):
  for j in range(i+1,len(l)):
    for k in range(j+1,len(l)):
      ans+=l[i]*l[j]*l[k]

print(ans)

