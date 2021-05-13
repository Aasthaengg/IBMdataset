_, c, k, *lst = map(int, open(0).read().split())
lst.sort()
res = 1
tmpt = lst[0]
tmpc = 0
for i in lst:
  tmpc += 1
  if not (tmpc <= c and i - tmpt <= k):
    res += 1
    tmpc = 1
    tmpt = i

print(res)