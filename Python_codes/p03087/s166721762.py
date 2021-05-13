N,Q=map(int,input().split())
S=input()
L=[0]*N
for i in range(1,N):
  if S[i-1]=="A" and S[i]=="C":
    L[i]=L[i-1]+1
  else:
    L[i]=L[i-1]
for i in range(Q):
  a,b=map(int,input().split())
  print(L[b-1]-L[a-1])