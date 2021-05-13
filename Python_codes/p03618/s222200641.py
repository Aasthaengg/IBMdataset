from collections import defaultdict

s = input()
n = len(s)

d = defaultdict(int)

ans = 1
for left_total, c in enumerate(s, 0):
    ans += left_total - d[c]
    d[c] += 1
print(ans)
