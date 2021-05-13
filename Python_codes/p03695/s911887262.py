_ = input()
a = [int(x) for x in input().split()]

p = set()
q = 0
for i in a:
    if i < 3200:
        p.add(i//400)
    else:
        q += 1
else:
    lenp = len(p)
    print(max(lenp, 1), lenp + q)