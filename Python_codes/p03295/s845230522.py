N,M=map(int,input().split())
x=[[0 for i in range(2)] for i in range(M)]
for i in range(M):
  a,b=map(int,input().split())
  x[i][0]=b
  x[i][1]=a
x.sort()
count=0
bmax=-1
for i in range(M):
  if(bmax<=x[i][1]):
    count+=1
    bmax=x[i][0]
#print(x)
print(count)