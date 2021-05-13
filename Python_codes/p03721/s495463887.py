n, k = map(int, input().split())
dic = {}
for i in range(n):
  a, b = map(int, input().split())
  dic.setdefault(a, 0)
  dic[a] += b
lst = sorted(list(dic.items()))
for tpl in lst:
  if k > tpl[1]:
    k -= tpl[1]
  else:
    print(tpl[0])
    exit()