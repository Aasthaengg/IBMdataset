from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
d = c.most_common()[::-1]

ans = 0
for i in range(len(set(A))-K):
    ans += d[i][1]

print(ans)