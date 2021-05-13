n, k = map(int, input().split())
must = k
rest = n - must
if k == 1:
    print(0)
else:
    print(rest)
