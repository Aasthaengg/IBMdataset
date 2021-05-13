N = int(input())
A = [0 for i in range(1001)]
mod = 10 ** 9 + 7
for n in range(2, N+1):
  m = n
  k = 2
  while m > 1:
    while m % k == 0:
      m //= k
      A[k] += 1
    k += 1
ans = 1
for i in range(1, 1001):
  ans = ans * (A[i] + 1) % mod
print(ans)