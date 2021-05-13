n = 1
N = int(input())
K = int(input())
for _ in range(N):
  if n > K:
    n += K
  else:
    n *= 2
print(n)