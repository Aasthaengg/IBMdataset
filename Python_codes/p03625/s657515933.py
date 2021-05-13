n = int(input())
a = list(map(int,input().strip().split()))

import collections

c = sorted(collections.Counter(a).items(), reverse=True)

leng_1 = 0
for leng,count in c:
  if count >=4:
    if leng_1 != 0:
      print(leng_1 * leng)
      exit()
    else:
      print(leng**2)
      exit()
  elif count >=2:
    if leng_1 != 0:
      print(leng_1*leng)
      exit()
    else:
      leng_1 = leng
print(0)