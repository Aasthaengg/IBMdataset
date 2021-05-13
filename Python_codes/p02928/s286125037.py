MOD = 10**9+7
n, k, *a = map(int, open(0).read().split())
s = t = 0
for i in range(n):
  s += sum(j>i and a[j]<a[i] for j in range(n))
  t += sum(a[j]<a[i] for j in range(n))
print((s*k + k*~-k//2*t) % MOD)