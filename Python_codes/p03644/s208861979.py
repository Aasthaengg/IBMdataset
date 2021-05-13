N=int(input())
res=[]
for i in range(0,N+1) :
  if N>=2**i :
    res.append(2**i)
print(res[-1])