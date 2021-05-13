n = int(input())
l, r = 0, 10 ** 4
while r - l > 1:
    m = (l + r) // 2
    if m * (m - 1) // 2 <= n:
        l = m
    else:
        r = m
if l * (l - 1) // 2 != n:
    print('No')
else:
    print('Yes')
    print(l)
    a = [[] for _ in range(l)]
    t = 1
    for i in range(l):
        for j in range(i + 1, l):
            a[i].append(t)
            a[j].append(t)
            t += 1
    for x in a:
        print(len(x), end=' ')
        print(' '.join(map(str, x)))
