import sys
input = sys.stdin.buffer.readline

from collections import defaultdict

N, A, B = map(int, input().split())
V = list(map(int, input().split()))
MOD = 10 ** 100 + 7

g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]
 
def comb(n, r, mod):
  if r < 0 or r > n:
    return 0
  r = min(r, n - r)
  return g1[n] * g2[r] * g2[n - r] % mod
 
for i in range(2, 50 + 1):
  g1.append((g1[-1] * i) % MOD)
  inverse.append((-inverse[MOD % i] * (MOD // i) ) % MOD)
  g2.append((g2[-1] * inverse[-1]) % MOD)

V = sorted(V)[::-1]
counter = defaultdict(int)

answer_ave = sum(V[:A]) / A
print(answer_ave)

for v in V:
  if v >= V[A]:
    counter[v] += 1
  else:
    break
counter = list(counter.items())
counter = sorted(counter)[::-1]
 
if len(counter) == 1:
  answer = 0
  for i in range(A, min(B + 1, counter[0][1] + 1)):
    answer += comb(counter[0][1], i, MOD)
  print(answer)
else:
  take = 0
  for i in range(len(counter) - 1):
    take += counter[i][1]
  answer = comb(counter[-1][1], A - take, MOD)
  print(answer)