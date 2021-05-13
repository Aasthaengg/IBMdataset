n = int(input())
s = input()
li_s = list(s)

import collections
c = collections.Counter(li_s)
cci = c.items()
#print(cci)
tmp = 1
for cc in cci:
    #print(cc[1])
    tmp *= (cc[1]+1)
print((tmp-1)%(10**9+7))