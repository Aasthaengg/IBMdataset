N, M = map(int, input().split())
A = []
B = []
for i in range(N):
  a = str(input())
  A.append(a)
for i in range(M):
  b = str(input())
  B.append(b)
  
flag = False
for i in range(N-M+1):
  for j in range(N-M+1):
    if A[i][j:j+M] == B[0]:
      k = 1
      while k < M:
        if A[i+k][j:j+M] == B[k]:
          k += 1
        else:
          break
      if k == M:
        flag = True
        break
        
if flag:
  print('Yes')
else:
  print('No')