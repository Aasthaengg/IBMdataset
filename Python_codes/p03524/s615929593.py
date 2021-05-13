S = input()
N = len(S)

from collections import Counter

c = Counter(S)

items = sorted(c.items(), key=lambda x: x[1])

if N == 1:
    print('YES')
elif N == 2:
    if len(items) == 1:
        print('NO')
    else:
        print('YES')
else:
    if len(items) < 3:
        print('NO')
    else:
        min = items[0][1]
        max = items[-1][1]
        if max - min >= 2:
            print('NO')
        else:
            print('YES')
