from collections import defaultdict

N = int(input())
V = list(map(int, input().split()))

d1 = defaultdict(int)
d2 = defaultdict(int)
for i, v in enumerate(V):
    if i % 2 == 0:
        d1[v] += 1
    else:
        d2[v] += 1
d1 = sorted(d1.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
d2 = sorted(d2.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

best = 10 ** 10
for d1, d2 in ((d1, d2), (d2, d1)):
    ans = N // 2 - d1[0][1]
    val = d1[0][0]
    if d2[0][0] != val:
        ans += N // 2 - d2[0][1]
    else:
        ans += d2[0][1]
        if 2 < len(d2):
            ans += N // 2 - d2[0][1] - d2[1][1]
    best = min(best, ans)
print(best)