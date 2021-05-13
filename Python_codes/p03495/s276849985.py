from collections import Counter

n, k = map(int, input().split())
num_lists = list(map(int, input().split()))

num_counts = dict()
length = len(set(num_lists))
ans = 0

if length > k:
  d = Counter()
  d.update(num_lists)
  count_sorted = list(d.values())
  count_sorted.sort()
  for i in range(length - k):
    ans += count_sorted[i]

print(ans)