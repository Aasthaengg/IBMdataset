from collections import defaultdict
h, w = map(int, input().split())

a = [list(input()) for _ in range(h)]
d = defaultdict(int)
for i in range(h):
    for j in range(w):
        d[ord(a[i][j]) - ord('a')] += 1

odd = 0
two = 0
four = 0
for i in range(26):
    four += d[i] // 4
    d[i] %= 4
    if d[i] % 2 == 0:
        two += d[i] // 2
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
