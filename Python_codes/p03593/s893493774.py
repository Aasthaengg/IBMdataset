from collections import Counter
h, w = map(int, input().split())
s = ''
for i in range(h):
    s += input()
c = list(Counter(s).values())
for i in range(len(c)):
    c[i] %= 4
a, b, c, d = c.count(0), c.count(1), c.count(2), c.count(3)
if b + d >= 2:
    print('No')
else:
    x = c + d
    if h % 2:
        x -= w // 2
    if w % 2:
        x -= h // 2
    if x <= 0:
        print('Yes')
    else:
        print('No')
