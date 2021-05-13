N, Q = map(int,input().split())
S = input()
R = [0]*(N+1)
A = False
C = False
for i in range(0,N):
  char = S[i]
  if char == 'A':
    A = True
  elif char == 'C' and A:
    R[i+1]+=1
    A = False
  else:
    A = False
  R[i+1]+=R[i]
for _ in range(Q):
  l, r = map(int,input().split())
  print(R[r]-R[l])
