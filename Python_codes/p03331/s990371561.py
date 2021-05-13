N = int(input())

cdt = None
for a in range(1, N):
    b = N - a
    x = sum([int(c) for c in str(a)]) + sum([int(c) for c in str(b)])
    if cdt is None or cdt > x:
        cdt = x
print(cdt)