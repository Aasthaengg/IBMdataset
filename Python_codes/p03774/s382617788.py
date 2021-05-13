N,M=map(int,input().split())
S=[]
for i in range(N):
  a,b=map(int,input().split())
  S.append((a,b))
P=[]
for i in range(M):
  c,d=map(int,input().split())
  P.append((c,d)) 
for i in range(N):
  D=10**9
  ans=0
  for j in range(M-1,-1,-1):
    if D>=(abs(S[i][0]-P[j][0])+abs(S[i][1]-P[j][1])):
      D=(abs(S[i][0]-P[j][0])+abs(S[i][1]-P[j][1]))
      ans=j
  print(ans+1)   