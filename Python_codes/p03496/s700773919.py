N, *A = map(int, open(0).read().split())

ma = max(A)
mi = min(A)

if abs(mi) <= abs(ma):
    p = A.index(ma)
    ans = [(p, i) for i in range(N)]
    ans += [(i - 1, i) for i in range(1, N)]
else:
    p = A.index(mi)
    ans = [(p, i) for i in range(N)]
    ans += [(i, i - 1) for i in reversed(range(1, N))]

print(len(ans))
for x, y in ans:
    print(x + 1, y + 1)