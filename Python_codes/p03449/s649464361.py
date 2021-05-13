N = int(input())
A = [list(map(int, input().split())) for i in range(2)]
s = []
if N == 1:
  ans = A[0][0]+A[1][0]
  print(ans)
  
else:
  for i in range(N-1):
    a = 0
    for j in range(i+1):
      a += A[0][j]
    for j in range(i,N):
      a += A[1][j]
    s.append(a)
  ans = max(s)
  print(ans)