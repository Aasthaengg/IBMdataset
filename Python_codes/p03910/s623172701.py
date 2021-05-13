N = int(input())
K = 0
k = 0
while K < N:
  k += 1
  K += k
while N > 0:
  if N >= k:
    print(k)
    N -= k
  k -= 1