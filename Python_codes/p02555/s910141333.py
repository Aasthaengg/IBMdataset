s = int(input())
mod = 10 ** 9 + 7

fact = [1] * s
inv = [1] * s
invf = [1] * s
for i in range(2, s):
  fact[i] = fact[i-1] * i % mod
  inv[i] = -(mod // i) * inv[mod % i] % mod
  invf[i] = invf[i-1] * inv[i] % mod

count = 0
rest = s
for n in range(1, s // 3 + 1):
  rest -= 3
  count = (count + fact[rest + n - 1] * invf[rest] * invf[n - 1]) % mod
print(count)