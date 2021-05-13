N, M = map(int, input().split())
A = []
B = []
C = []
flag = 0

for i in range(N):
  A.append(input())
for i in range(M):
  B.append(input())

for i in range(N- M+ 1):
  for j in range(N- M+ 1):
    C = []
    for k in range(M):
      C.append(A[j+ k][i:i+ M])
    if(B == C):
      print("Yes")
      flag = 1
      break
  if(flag == 1):
    break
else:
  print("No")