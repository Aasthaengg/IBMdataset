
MOD = 10 ** 9 + 7

N, K = map(int, input().split())

A = list(map(int, input().split()))

totalMin = [0] * N
afterMin = [0] * N

def addAll(n):
  return (n * (n + 1) // 2) % MOD


for i in range(N):
  for j in range(N):
    if A[i] > A[j]:
      if i < j:
        afterMin[i] += 1
      totalMin[i] += 1

total = 0
for i in range(N):
  total = (total + afterMin[i] * K) % MOD
  total = (total + totalMin[i] * addAll(K - 1)) % MOD

print(total)
