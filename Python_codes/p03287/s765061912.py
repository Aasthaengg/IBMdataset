from collections import Counter
n, m = map(int, input().split())
c = Counter()
now = 0
c[now] += 1
ans = 0
for a in map(int, input().split()):
    now = (now + a) % m
    ans += c[now]
    c[now] += 1
print(ans)
