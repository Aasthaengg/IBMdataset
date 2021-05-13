n = int(input())
alst = list(map(int, input().split()))
blst = list(map(int, input().split()))
if sum(alst) - sum(blst) < 0:
    print(-1)
    exit()


ans = 0
res = []
plus = 0
for a, b in zip(alst, blst):
    if a < b:
        ans += 1
        plus += b - a
    else:
        res.append(a - b)
res.sort(reverse = True)
pos = 0
while plus > 0:
    plus -= res[pos]
    ans += 1
    pos += 1
print(ans)