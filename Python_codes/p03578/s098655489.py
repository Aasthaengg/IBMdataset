from collections import Counter

n = int(input())
d = Counter(list(map(int, input().split())))
m = int(input())
t = Counter(list(map(int, input().split())))

Make = True
for i, j in t.items():
    if d[i] < j:
        Make = False

if Make:
    print('YES')
else:
    print('NO')