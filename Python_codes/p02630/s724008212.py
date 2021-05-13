from collections import defaultdict

n = int(input())
arr = list(input().split())
q = int(input())
num_counts = defaultdict(lambda: 0)
ans = 0

for i in arr:
  num_counts[i] += 1
  ans += int(i)

for _ in range(q):
  bef, af = list(input().split())
  apper_count = num_counts[bef]
  ans += (int(af) - int(bef)) * apper_count
  num_counts[bef] -= apper_count
  num_counts[af] += apper_count
  print(ans)
