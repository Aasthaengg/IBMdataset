A, B, K = map(int, input().split())
ans = []

if B + 1 - A < 2 * K:
  ans = [i for i in range(A, B + 1)]
else:
  ans = [i for i in range(A, A + K)] + [i for i in range(B + 1 - K, B + 1)]
for a in ans:
  print(a)