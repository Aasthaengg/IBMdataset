n = int(input())
a = list(map(int, input().split()))

w = []
num = 0
for i in a:
    if 1 <= i <= 399:
        if 1 not in w:
            w.append(1)
    elif 400 <= i <= 799:
        if 400 not in w:
            w.append(400)
    elif 800 <= i <= 1199:
        if 800 not in w:
            w.append(800)
    elif 1200 <= i <= 1599:
        if 1200 not in w:
            w.append(1200)
    elif 1600 <= i <= 1999:
        if 1600 not in w:
            w.append(1600)
    elif 2000 <= i <= 2399:
        if 2000 not in w:
            w.append(2000)
    elif 2400 <= i <= 2799:
        if 2400 not in w:
            w.append(2400)
    elif 2800 <= i <= 3199:
        if 2800 not in w:
            w.append(2800)
    else:
        num += 1
if 0 < len(w):
    print(len(w), len(w)+num)
else:
    print(1, len(w)+num)