import sys
read=sys.stdin.buffer.read
readline=sys.stdin.buffer.readline
readlines=sys.stdin.buffer.readlines

N,M,L=map(int,readline().split())
#print("N M L:",N,M,L)

root=[[10**10 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
  A,B,C=map(int,readline().split())
  root[A][B],root[B][A]=C,C
  
Q=int(readline())
S,T=[0]*Q,[0]*Q
for i in range(Q):
  S[i],T[i]=map(int,readline().split())
#print("root:",root)
#print("S:",S)
#print("T:",T)

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      root[i][j]=min(root[i][j],root[i][k]+root[k][j])
#print("root:",root)
for i in range(1,N+1):
  for j in range(1,N+1):
    if root[i][j]<=L:
      root[i][j]=1
    else:
      root[i][j]=10**10
#print("root(1):",root)

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      if root[i][k]!=-1 and root[k][j]!=-1:
        root[i][j]=min(root[i][j],root[i][k]+root[k][j])
#print("root(2):",root)

for i in range(Q):
  print(root[S[i]][T[i]]-1 if root[S[i]][T[i]]<10**10 else -1)