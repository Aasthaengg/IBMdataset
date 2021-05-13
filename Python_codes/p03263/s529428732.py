h, w = map(int, input().split())
a = [list(map(int , input().split())) for _ in range(h)]

res = []
for hi in range(h):
    for wi in range(w-1):
        if a[hi][wi] % 2 == 1:
            a[hi][wi] -= 1
            a[hi][wi+1] += 1
            res.append((hi+1, wi+1, hi+1, wi+1+1))
for hi in range(h-1):
    wi = w - 1
    if a[hi][wi] % 2 == 1:
        a[hi][wi] -= 1
        a[hi+1][wi] += 1
        res.append((hi+1, wi+1, hi+1+1, wi+1))

print(len(res))
for resi in res:
    print(' '.join(map(str, resi)))
