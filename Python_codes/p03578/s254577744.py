n = int(input())
D = tuple(map(int, input().split()))
m = int(input())
T = tuple(map(int, input().split()))

from collections import Counter
CD = Counter(D)
CT = Counter(T)
for t, ct in CT.items():
    cd = CD[t]
    if ct > cd:
        print('NO')
        break
else:
    print('YES')
