s = [input() for i in range(4)]
coin500 = int(s[0]) 
coin100 = int(s[1])
coin50 = int(s[2])

list = []
for i in range(coin500 + 1):
  for j in range(coin100 + 1):
    for k in range(coin50 + 1):
      list.append(500 * i + 100 * j + 50 * k)

import collections
c = collections.Counter(list)
if c.get(int(s[3])) == None:
    print("0")
else:
    print(c.get(int(s[3])))