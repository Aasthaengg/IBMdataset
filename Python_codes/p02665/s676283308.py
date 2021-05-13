N = int(input())
A = list(map(int, input().split()))

if N == 0 and A[0] != 1:
  print(-1)
elif N != 0 and A[0] != 0:
  print(-1)
else:
  ans = 1
  nodes = 1
  preF = 0
  sucF = sum(A)
  
  for d in range(1, N+1):
    fol = A[d]
    nodes = min((nodes-preF)*2, sucF)
    
    if nodes < fol:
      print(-1)
      exit()
    
    ans += nodes
    preF = fol
    sucF -= fol
  print(ans)