from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
cntr = Counter(lst)
res = 0
for i in cntr:
  if cntr[i] >= i:
    res += (cntr[i] - i)
  else:
    res += cntr[i]
print(res)