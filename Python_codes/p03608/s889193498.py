N,M,C=[int(x) for x in str(input()).split()]
r=[int(x) for x in str(input()).split()]
ABC=[[0 for i in range(4)]]

dis=[[1000000000000 for i in range(N+1)]]

for i in range(N):
  dis.append([1000000000000 for i in range(N+1)])


for i in range(M):
  x=[0]+[int(x) for x in str(input()).split()]
  ABC.append(x)
  dis[x[1]][x[2]]=x[3]
  dis[x[2]][x[1]]=x[3]
  y=[0,x[2],x[1],x[3]]
  ABC.append(y)

for i in range(1,N+1):
  dis[i][i]=0


for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])


mi=1000000000000
def perm(a,i):
  global mi
  if i==len(a):      

    p=0
    for x in range(len(a)-1):
      p+=dis[a[x]][a[x+1]]

    mi=min(mi,p)


  else:
    for j in range(i,len(a)):
      a[i],a[j]=a[j],a[i]
      perm(a,i+1)
      a[i],a[j]=a[j],a[i]


perm(r,0)

print(mi)
