N=int(input())
if N==1:
  print(1)
  exit()
L=list()
R=list()
for i in range(N):
  a,b=map(int,input().split())
  L.append([a,b])
k=dict()
for i in range(N-1):
  for j in range(i+1,N):
    a,b=L[i]
    c,d=L[j]
    R.append([a-c,b-d])
    n=str(a-c)+" "+str(b-d)
    if n in k:
      k[n]+=1
    else:
      k[n]=1
    R.append([c-a,d-b])
    n=str(c-a)+" "+str(d-b)
    if n in k:
      k[n]+=1
    else:
      k[n]=1
op=max(k.values())
print(N-op)