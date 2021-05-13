from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))

accum = [0] * (n + 1)

for i in range(n):
  accum[i + 1] = accum[i] + A[i]
  
box = defaultdict(int)

for i in accum:
  box[i % m] += 1
  
ans = 0
for v in box.values():
  ans += v * (v - 1) // 2
  
print(ans)