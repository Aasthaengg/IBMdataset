from collections import Counter
x = Counter()
for _ in range(3):
    a,b = input().split()
    x[a] += 1
    x[b] += 1
if len(x) == 4 and max(x.values()) != 3:
    print('YES')
else:
    print('NO')