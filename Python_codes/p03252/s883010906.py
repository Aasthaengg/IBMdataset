s = input()
t = input()

f = True
for (s1, s2) in [(s, t), (t, s)]:
    d = dict()
    for c1, c2 in zip(s1, s2):
        if c1 not in d:
            d[c1] = c2
        elif d[c1] != c2:
            f = False
            break

if f:
    print('Yes')
else:
    print('No')
