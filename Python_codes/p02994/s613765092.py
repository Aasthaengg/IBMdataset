N, L = map(int, input().split())
l = range(L, N + L)
a = [sum(l[1:]), sum(l[:-1]), sum(l), sum(l)]
print(a[((0 in l) << 1) + (L < 0)])