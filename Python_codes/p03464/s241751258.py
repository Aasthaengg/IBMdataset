K, *A = map(int, open(0).read().split())

mi = ma = 2
for a in reversed(A):
    mi = -(-mi // a) * a
    ma = (ma // a) * a + a - 1

if ma < mi:
    print(-1)
else:
    print(mi, ma)
