from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
if len(c) > 3:
    print('No')
else:
    if len(c) == 1 and c.get(0):
        print('Yes')
    elif len(c) == 2 and c.get(0) == n / 3:
        print('Yes')
    elif len(c) == 3:
        x, y, z = c.keys()
        if x^y^z == 0 and c.get(x) == c.get(y) == c.get(z) == n / 3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
