from collections import Counter
h, w, *s = open(0).read().split()
h = int(h)
w = int(w)

s = Counter(''.join(s))

odd = 0
two = 0
four = 0
for k, v in s.items():
    four += v // 4
    v %= 4
    if v % 2 == 0:
        two += v // 2
    else:
        odd += 1
if h % 2 == 1 and w % 2 == 1:
    if odd == 1 and two <= h // 2 + w // 2:
        print('Yes')
    else:
        print('No')
elif h % 2 == 1:
    if odd == 0 and two <= w // 2:
        print('Yes')
    else:
        print('No')
elif w % 2 == 1:
    if odd == 0 and two <= h // 2:
        print('Yes')
    else:
        print('No')
else:
    if odd == 0 and two == 0:
        print('Yes')
    else:
        print('No')
