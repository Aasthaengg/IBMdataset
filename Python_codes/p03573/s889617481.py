from collections import Counter
l = [int(i) for i in input().split()]
c = dict(Counter(l))
for k, v in c.items():
    if v == 1:
        print(k)