N = int(input())

mod = 10 ** 9 + 7

now = 1
for i in range(N):
  now *= (i + 1)
  now %= mod
  
print(now)