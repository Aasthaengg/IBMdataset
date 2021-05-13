A = list(input())
N = len(A)

ans = N * (N - 1) // 2 + 1

R = {}
for a in A:
  if a not in R: R[a] = 1
  else: R[a] += 1

for n in R.values():
  ans -= n * (n - 1) // 2

print(ans)