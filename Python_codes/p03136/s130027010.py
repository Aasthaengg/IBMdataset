n, *l = map(int, open(0).read().split())

a = sorted(l, reverse=True)
b, c = a[0], sum(a[1:])
if b < c:
    print('Yes')
else:
    print('No')
