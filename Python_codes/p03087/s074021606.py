N,Q = map(int,input().split())
S = input()
X = [list(map(int, input().split())) for _ in range(Q)]
L =[0]*(N+1)
for i in range(N-1):
  if S[i]=="A" and S[i+1]=="C":
    L[i+1] = L[i]+1 
  else:
    L[i+1] = L[i]
L[N] = L[N-1]
for x in X:
  print(L[x[1]-1]-L[x[0]-1])