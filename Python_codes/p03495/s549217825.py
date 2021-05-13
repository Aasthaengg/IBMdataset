from collections import Counter

n, k = map(int, input().split())
a = input().split()
d = sorted(Counter(a).values())
ans = 0

for i in range(len(d) - k):
    ans += d[i]

print(ans)