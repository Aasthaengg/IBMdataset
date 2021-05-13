from collections import Counter

A = Counter(list(input().split()))
for k, v in A.items():
  if v == 1:
    print(k)
    exit()