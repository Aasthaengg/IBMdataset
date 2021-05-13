from collections import defaultdict

m = defaultdict(int)

n = int(input())

for _ in range(n):
  m[input()] += 1

for k in ["AC", "WA", "TLE", "RE"]:
  print(f"{k} x {m[k]}")