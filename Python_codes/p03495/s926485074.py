n,k=map(int,input().split())
a=list(map(int,input().split()))
x=[0 for i in range(n)]
y=[]
s=0
for i in range(n):
  x[a[i]-1]+=1
    
for i in range(n):
  if x[i]:
    y.append(x[i])
y.sort()
z=len(y)
i=0
while(z>k):
  s+=y[i]
  z-=1
  i+=1
print(s)