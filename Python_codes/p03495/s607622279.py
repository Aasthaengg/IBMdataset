# AtCoder
from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))
c = Counter(A)
k = sorted(c.most_common(), reverse=True, key=lambda x: x[1])[K:]

ans = 0
for e in k:
    ans += e[1]
print(ans)
