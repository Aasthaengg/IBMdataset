N, K = map(int, input().split())
L = list(map(int, input().split()))

from collections import Counter
C = Counter(L).most_common()

ans = 0
for i, item in enumerate(C):
    if i < K:
        continue;
    ans += item[1]

print(ans, flush=True)
