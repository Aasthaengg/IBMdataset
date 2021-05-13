from collections import Counter

n = int(input())
s = list(input())

ans = 0

for i in range(1, n - 1):
    ans = max(ans, len(Counter(s[:i]).keys() & Counter(s[i:]).keys()))

print(ans)
