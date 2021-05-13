from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))
d = Counter(a)
d = d.most_common()
ans = 0

for i in range(len(d) - k):
    ans += d[-i - 1][1]

print(ans)