N,M,X=map(int,input().split())
A=list(map(int,input().split()))
d=[0]*(N+1)
j=0
for i in range(A[0],N+A[0]):
  try:
    if i==A[j]:
      d[i]+=1
      j+=1
  except:
    pass
#print(d)
print(min(sum(d[:X]),sum(d[X:])))