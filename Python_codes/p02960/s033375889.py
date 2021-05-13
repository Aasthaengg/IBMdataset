from collections import defaultdict

S = input()
N = len(S)

MOD = 10**9 + 7
mod = 13

A = [1, 10, 9, 12, 3, 4]
D = defaultdict(int)
a = 0

for i in range(N):
  if S[-1-i] == "?":
    D[A[i%6]] += 1
  else:
    a += A[i%6] * int(S[-1-i]) % mod
    a %= mod

ans = [0]*mod
ans[0] = 1

for i, x in D.items():
  for _ in range(x):
    prev = [a for a in ans]
    ans = [0]*mod
    for j in range(mod):
      for y in range(10):
        ans[(j+i*y)%mod] += prev[j]
      ans = [a%MOD for a in ans]

print(ans[(5-a)%mod])