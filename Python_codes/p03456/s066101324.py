from math import sqrt
a, b = map(int, input().split())
x = str(a) + str(b)
x = int(x)
f = sqrt(x)
d = f - int(f)
if d!=0:
    print('No')
else:
    print('Yes')