from collections import Counter
n = int(input())
c = Counter(input().split())
ans = 0
for q, w in c.items():
    q, w = int(q), int(w)
    ans += w - q if q < w else (w if q != w else 0)
print(ans)