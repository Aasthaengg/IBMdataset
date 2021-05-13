n, h, w, *a = list(map(int, open(0).read().split()))

ans = 0
for a, b in zip(*[iter(a)]*2):
    ans += not(a < h or b < w)
print(ans)