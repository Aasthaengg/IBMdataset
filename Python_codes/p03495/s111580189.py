import collections
n, k = map(int, input().split())
a_lst = list(map(int, input().split()))

c = collections.Counter(a_lst)
res = 0
sorted_c = sorted(c.items(), key=lambda x:x[1])
if len(c) <= k:
  print(res)
  quit()
else:
  for k, v in sorted_c[:(len(c) - k)]:
    res += v
print(res)
