from operator import itemgetter
n = int(input())
dic = {}
for i in range(1, n + 1):
  s, p = input().split()
  p = int(p)
  dic.setdefault(s, [])
  dic[s].append((i, p))
cities = sorted(list(dic.keys()))
for c in cities:
  dic[c].sort(key=itemgetter(1), reverse=True)
  for i in dic[c]:
    print(i[0])