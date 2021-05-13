from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

if len(set(a)) == 1 and list(set(a))[0] == 0:
    print('Yes')
    exit()

if n % 3 == 0 and len(set(a)) == 3:
    x = list(set(a))
    e = x[0]
    b = x[1]
    c = x[2]
    if e ^ b != c:
        print('No')
        exit()
    if b ^ c != e:
        print('No')
        exit()
    if c ^ e != b:
        print('No')
        exit()
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    if d[e] != d[b] or d[b] != d[c] or d[c] != d[e]:
        print('No')
        exit()
    print('Yes')
elif n % 3 == 0 and len(set(a)) == 2:
    x = list(set(a))
    x.sort()
    if x[0] == 0:
        t = 1
    else:
        print('No')
        exit()
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    if d[x[0]]*2 == d[x[1]]:
        print('Yes')
        exit()
    print('No')
else:
    print('No')