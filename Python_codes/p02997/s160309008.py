from itertools import combinations

N, K = map(int, input().split())

if K > (N-1)*(N-2)//2:
  print(-1)
else:
  M = N*(N-1)//2 - K
  print(M)
  for i in range(2, N+1):
    print(1, i)
  M -= N-1
  for ab in combinations(range(2, N+1), 2):
    if M == 0:
      break
    else:
      a, b = ab
      print(a, b)
      M -= 1