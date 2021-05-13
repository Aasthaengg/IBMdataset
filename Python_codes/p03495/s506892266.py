from collections import Counter

N,K,*a = map(int, open(0).read().split())
c = Counter(a)
v = sorted([x for x in c.values()])
if len(v) - K > 0:
    print(sum(v[:len(v)-K]))
else:
    print(0)