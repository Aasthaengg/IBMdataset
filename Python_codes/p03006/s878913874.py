N=int(input())
x=[0]*N
y=[0]*N
for i in range(N):
  x[i],y[i] = map(int,input().split() )
d=dict()

maxi=0
for i in range(N-1):
  for j in range(i+1,N):
    if (x[j]-x[i],y[j]-y[i]) not in d:
      d[ (x[j]-x[i],y[j]-y[i]) ] =1
      d[ (x[i]-x[j],y[i]-y[j]) ] =1
    else:
      d[ (x[j]-x[i],y[j]-y[i]) ] +=1
      d[ (x[i]-x[j],y[i]-y[j]) ] +=1
#print(d)      

for p in d:
  maxi=max(maxi,d[p])
ans= (N-1-maxi)+1
print(ans)
