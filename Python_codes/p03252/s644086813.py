ss,tt = open(0).read().split()

from collections import defaultdict

d = defaultdict(str)
e = defaultdict(str)
ans = 'Yes'
for s,t in zip(ss,tt):
    if not d[s]:
        d[s] = t
    elif d[s] != t:
        ans = 'No'
        break
    if not e[t]:
        e[t] = s
    elif e[t] != s:
        ans = 'No'
        break

print(ans)