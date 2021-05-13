from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * (n + 1)
for i, ai in enumerate(a):
    s[i + 1] = (s[i] + ai) % m

counter = Counter(s)
ans = 0
for v in counter.values():
    ans += v * (v - 1) // 2

print(ans)