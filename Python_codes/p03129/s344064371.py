N, K = map(int, input().split())

if N % 2 == 1:
  if len([i for i in range(N+1) if i % 2 == 1]) >= K:
    print("YES")
  else:
    print("NO")
else:
  if len([i for i in range(N) if i % 2 == 1]) >= K:
    print("YES")
  else:
    print("NO")
