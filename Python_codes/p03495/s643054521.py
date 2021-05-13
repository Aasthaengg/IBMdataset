from collections import Counter
n, k = map(int, input().split())
cntr = Counter(list(map(int, input().split())))
if len(cntr) <= k:
  print(0)
  exit()
freq = sorted(list(cntr.values()))
print(sum(freq[:len(freq) - k]))