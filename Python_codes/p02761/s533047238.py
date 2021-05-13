n,m=[int(x) for x in input().split()]
a=0
S=0
L=[]
for i in range(m):
  s,c=[int(x) for x in input().split()]
  L.append([s,c])
if n!=1:
  for i in range(10**(n-1),10**n):
    I=str(i)
    l=[]
    for j in range(m):
      s,c=L[j][0],L[j][1]
      if I[s-1]!=str(c):
        l.append(False)
    if l==[]:
      ans=i
      a=1
      break
else:
  for i in range(10**n):
    I=str(i)
    l=[]
    for j in range(m):
      s,c=L[j][0],L[j][1]
      if I[s-1]!=str(c):
        l.append(False)
    if l==[]:
      ans=i
      a=1
      break
if a==0:
  print(-1)
elif a==1:
  print(ans)