s = input()
t = input()

import bisect
from collections import defaultdict
d = defaultdict(list)
for i in range(len(s)):
    d[s[i]].append(i)

#print(d)
now=-1
cnt=0
for i in range(len(t)):
    if len(d[t[i]])==0:
        print(-1)
        exit()

    ind = bisect.bisect_right(d[t[i]],now)
#    print(now,ind)
    if ind==len(d[t[i]]):
        ind = bisect.bisect_right(d[t],0)
        cnt+=1
#    print(t[i],cnt)
    now=d[t[i]][ind]

print(cnt*len(s) +now +1)

#print(cnt,len(s), d[t[-1]])