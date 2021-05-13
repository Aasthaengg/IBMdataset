from collections import Counter

N = int(input())
b = list(map(int, input().split()))
cntr = Counter(b)

out = 0
for k, v in cntr.items():
  if v>k:
    out += v-k
  elif v<k:
    out += v
print(out)