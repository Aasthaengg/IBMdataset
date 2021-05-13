N=int(input())
K=int(input())

n=1
for i in range(N):
  if 2*n >= n + K: n += K
  else: n *= 2

print(n)