from collections import Counter

n, k = map(int, input().split())
L = list(map(int, input().split()))
cnt = Counter(L)
if len(cnt.keys()) <= k:
  print(0)
else:
  rewrite_groups = len(cnt.keys()) - k
  print(sum(sorted(cnt.values())[:rewrite_groups]))