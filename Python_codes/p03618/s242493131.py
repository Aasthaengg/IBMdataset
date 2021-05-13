a = input()
d = {}
for i in a:
    if i not in d.keys():
        d[i] = 0
    d[i]+=1

import itertools
ans = 0
for l in itertools.combinations(d.values(),2):
    x,y = l[0],l[1] 
    ans+=(x*y)
print(ans+1)