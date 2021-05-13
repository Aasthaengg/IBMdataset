from collections import Counter
from itertools import combinations
N = int(input())
S = [input()[0] for _ in range(N)]
cnt = Counter(S)
ans = 0
for a, b, c in combinations('MARCH', 3):
    ans += cnt[a] * cnt[b] * cnt[c]

print(ans)