N,K = [ int(it) for it in input().split() ]

li=[0]*K
for i in range(1,N+1):
  if (i*2)%K==0:
    li[i%K]+=1
print ( sum( [ v**3 for v in li ] ) )