N,C = [ int(it) for it in input().split() ]
li = [ [ int(it) for it in input().split() ] for i in range(N) ]

dx = [0]*(N+1)
for i in range(N+1):
  if (i==0):
    dx[i]=li[i][0]-0
  elif(i==N):
    dx[i]=C-li[i-1][0]
  else:
    dx[i]=li[i][0]-li[i-1][0]

lic = [0]*(N+1)
for i in range(N):
  lic[i+1] = lic[i] + li[i][1] - dx[i]
liu = [0]*(N+1)
for i in range(N,0,-1):
  liu[i-1] = liu[i] + li[i-1][1] - dx[i]
lic2 = [0]*(N+1)
for i in range(N):
  lic2[i+1] = lic2[i] + li[i][1] - dx[i]*2
liu2 = [0]*(N+1)
for i in range(N,0,-1):
  liu2[i-1] = liu2[i] + li[i-1][1] - dx[i]*2
lic2ma = [0]*(N+1)
for i in range(1,N+1):
  lic2ma[i] = max(lic2ma[i-1],lic2[i])
liu2ma = [0]*(N+1)
for i in range(N-1,0,-1):
  liu2ma[i] = max(liu2ma[i+1],liu2[i])

if (False):
  
  print (dx)  
  print ( lic )
  print ( liu )  

  print (lic2)
  print (lic2ma)
  print (liu2)
  print (liu2ma)

ma = 0
for i in range(N+1):
  ma = max(ma, lic[i] + liu2ma[i] )
  ma = max(ma, liu[i] + lic2ma[i] )
  
print ( ma )

  


