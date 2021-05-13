N, K = map(int, input().split())
if N / 2 + 1 > K:
  print("YES")
elif N / 2 + 1 == K:
  if N % 2 != 0:
    print("YES")
  else:
    print("NO")
else:
  print("NO")