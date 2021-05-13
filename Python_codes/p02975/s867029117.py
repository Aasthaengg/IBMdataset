from collections import Counter
n = int(input())
a = [int(x) for x in input().split()]

d = Counter()
for x in a:
    d[x] += 1

if d[0] == n:
    print('Yes')
elif len(d.keys()) == 2 and d[0] == n//3:
    print('Yes' if d[0] == n//3 else 'No')
elif len(d.keys()) == 3:
    p, q, r = d.keys()
    if d[p] == d[q] and d[q] == d[r] and p ^ q ^ r == 0:
        print('Yes')
    else:
        print('No')
else:
    print('No')