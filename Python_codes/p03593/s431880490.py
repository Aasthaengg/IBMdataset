h, w = map(int, input().split())
a = {}
for i in range(h):
    s = input()
    for i in s:
        a.setdefault(i, 0)
        a[i] += 1
a2 = 0
a1 = 0
for i in a.values():
    if i % 2 == 1:
        a1 += 1
    elif i % 4 == 2:
        a2 += 2
if h % 2 == 1:
    if w % 2 == 1:
        b1 = 1
        b2 = h + w - 2
    else:
        b1 = 0
        b2 = w
else:
    if w % 2 == 1:
        b1 = 0
        b2 = h
    else:
        b1 = 0
        b2 = 0
if a1 > b1 or a2 > b2:
    print("No")
else:
    print("Yes")