n = int(input())
dic = {}
march = set(['M', 'A', 'R', 'C', 'H'])
for i in range(n):
  s = input()[0]
  if s in march:
    dic.setdefault(s, 0)
    dic[s] += 1
if len(dic) <= 2:
  print(0)
  exit()
march = ['M', 'A', 'R', 'C', 'H']
for t in march:
  dic.setdefault(t, 0)
march = ['MAR', 'MAC', 'MAH', 'MRC', 'MRH', 'MCH', 'ARC', 'ARH', 'ACH', 'RCH']
res = 0
for t in march:
  res += (dic[t[0]] * dic[t[1]] * dic[t[2]])
print(res)