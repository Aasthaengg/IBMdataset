N = int(input())
A = list(map(int, input().split()))
B = [0]*60
mod = 10 ** 9 + 7

for x in A:
  for i in range(60):
    B[i] += (x >> i) & 1

ans = 0
p = 1

for i in range(60):
  if i >= 1:
    p *= 2
    p %= mod
  ans += (N-B[i])*B[i]*p
  ans %= mod

print(ans)