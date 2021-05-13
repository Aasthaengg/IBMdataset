n, *a = map(int, open(0).read().split())
f = 0
t = 0
o = 0
for i in a:
    if i % 4 == 0:
        f += 1
    elif i % 2 == 0:
        t += 1
    else:
        o += 1
if f >= o - 1 and t == 0:
    print('Yes')
elif f >= o:
    print('Yes')
else:
    print('No')