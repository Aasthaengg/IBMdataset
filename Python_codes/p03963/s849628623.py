N, K = map(int, input().split())
ans = K

if N == 1:
  print(ans)
  
else:
  for i in range(N-1):
    ans *= K-1
    
  print(ans)