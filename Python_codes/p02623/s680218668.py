n, m, k = map(int, input().split())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))

asum = [0]
bsum = [0]

for i, new in enumerate(alst):
    if asum[i] + new <= k:
        asum.append(asum[i] + new)
    else:
        break
for i, new in enumerate(blst):
    if bsum[i] + new <= k:
        bsum.append(bsum[i] + new)
    else:
        break

bmax = len(bsum)-1
ans = 0

for i, atime in enumerate(asum):
    while atime + bsum[bmax] > k:
        bmax -= 1
    ans = max(ans, i+bmax)

print(ans)