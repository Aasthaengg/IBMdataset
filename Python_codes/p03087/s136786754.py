N,Q=map(int,input().split())
S=input()
L=[0]*N
p=S[0]
for i in  range(1,N):
  L[i]+=L[i-1]
  if p+S[i]=='AC':
    L[i]+=1
  p=S[i]
for _ in range(Q):
  i,j=map(int,input().split())
  print(L[j-1]-L[i-1])
