def tashi(n):
  c=str(n)
  return "0"*(6-len(c))+c
R=list()
N,M=map(int,input().split())
for i in range(M):
  P,Y=map(int,input().split())
  R.append([P,Y,i])
R=sorted(R)
f=1
k=0
for i in range(M):
  c=R[i]
  if c[0]==f:
    k+=1
    c.append(k)
  else:
    k=1
    c.append(k)
  f=c[0]
K=[0]*M
for i in range(M):
  c=R[i]
  K[c[2]]=tashi(c[0])+tashi(c[3])
for i in range(M):
  print(K[i])