n = int(input())
s = [input() for i in range(n)]

import collections
c = collections.Counter(s)
ans = []
most = c.most_common()
word,count = most[0]
ans.append(word)
for i in range(1,len(c)):
    wordi,counti = most[i]
    if counti == count:
        ans.append(wordi)
    else:
        break
ans.sort()
print(*ans, sep = "\n")