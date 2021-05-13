N=int(input())
d=[0]*N
for i in range(N) :
  d[i]=int(input())
d.sort()
count=1
for i in range(1,N) :
  if d[i-1]!=d[i] :
    count+=1
print(count)