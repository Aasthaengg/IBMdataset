n=int(input())
l=[list(map(int,input().split())) for i in range(n-1)]
connection=[[] for i in range(n)]
for i in range(n-1):
  connection[l[i][0]-1].append(l[i][1]-1)
  connection[l[i][1]-1].append(l[i][0]-1)

distance1=[-1 for i in range(n)]
distance1[0]=0
next=connection[0]
next2=[]
check=[-1 for i in range(n)]
check[0]=1
checkct=1
ct=0
while len(next)!=0 and checkct!=n:
  ct+=1
  for i in range(len(next)):
    distance1[next[i]]=ct
    check[next[i]]=1
    checkct+=1
    for j in range(len(connection[next[i]])):
      if check[connection[next[i]][j]]==-1:
        next2.append(connection[next[i]][j])
  next=next2
  next2=[]

distanceN=[-1 for i in range(n)]
distanceN[n-1]=0
next=connection[n-1]
next2=[]
check=[-1 for i in range(n)]
check[n-1]=1
checkct=1
ct=0
while len(next)!=0 and checkct!=n:
  ct+=1
  for i in range(len(next)):
    distanceN[next[i]]=ct
    check[next[i]]=1
    checkct+=1
    for j in range(len(connection[next[i]])):
      if check[connection[next[i]][j]]==-1:
        next2.append(connection[next[i]][j])
  next=next2
  next2=[]

ctF=0;ctS=0
for i in range(n):
  if distance1[i]<=distanceN[i]:
    ctF+=1
  else:
    ctS+=1
if ctF>ctS:
  print('Fennec')
else:
  print('Snuke')