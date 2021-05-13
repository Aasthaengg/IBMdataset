n = int(input())
l = list(map(int, input().split()))

from collections import Counter
c = Counter(l)
ans = 0
for key in c:
    if key > c[key]:
        ans += c[key]
    else:
        ans += c[key] - key

print(ans , flush=True)

