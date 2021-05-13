from math import log2, ceil
n, k = map(int, input().split())
dic = {}
for i in range(1, n + 1):
  x = max(0, ceil(log2(k / i)))
  dic.setdefault(x, 0)
  dic[x] += 1
res = 0
for i in dic:
  res += (dic[i] * (2 ** -i))
print(res / n)