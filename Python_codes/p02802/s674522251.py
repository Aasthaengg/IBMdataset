(N,M),*ps = [s.split() for s in open(0)]

ps = [(int(p),s=='WA') for p,s in ps]

from collections import Counter
cnt = Counter()
acs = set()

for p,s in ps:
    if p not in acs:
        if s:
            cnt[p] += 1
        else:
            acs.add(p)
a = len(acs)
b = sum(cnt[ac] for ac in acs)
print(a,b)