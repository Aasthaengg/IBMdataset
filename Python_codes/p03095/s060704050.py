N = int(input())
S = str(input())

from collections import Counter
freq = Counter(S)

div = int(1e9 + 7)
total = 1
for c in freq.keys():
  #print(c, freq[c])
  total = total * (freq[c] + 1) % div

ans = total - 1
print(ans)