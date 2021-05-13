from collections import Counter

N = int(input())
a = list(map(int, input().split()))

if len(set(a)) == 1 and a[0] == 0:
    print('Yes')
elif N % 3 == 0:
    l = [*Counter(a).values()]
    res = 0
    for s in set(a):
        res ^= s
    if len(l) == 3 and res == 0 and len(set(l)) == 1:
        print('Yes')
    elif len(l) == 2 and a.count(0) == N//3:
        print('Yes')
    else:
        print('No')
else:
    print('No')