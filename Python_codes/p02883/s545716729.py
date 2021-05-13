N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A = sorted(A)
F = sorted(F, reverse=True)

l = -1
r = 10**12+5

while (l+1<r):
  c = (l+r)//2
  tmp = 0
  for i in range(N):
    tmp += max(0, A[i]-(c//F[i]))
  
  if tmp <= K:
    r = c
  else:
    l = c

print(r)