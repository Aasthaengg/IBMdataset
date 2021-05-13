from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

div = [a[i] - b[i] for i in range(n)]

if sum(div) < 0:
    print(-1)
    exit()

div.sort()
idx = bisect_left(div, 0)
positive = div[idx:]
negative = div[:idx]

if idx == 0:
    print(0)
    exit()

ans = len(negative)
changed = False

for x in negative:
    x = abs(x)
    while x > positive[-1]:
        x -= positive.pop(-1)
        if not changed:
            ans += 1
        changed = False
    positive[-1] -= x
    if not changed:
        ans += 1
        changed = True

print(ans)
