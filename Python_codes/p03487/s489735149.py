n = int(input())
A = list(map(int, input().split()))

from collections import Counter
C = Counter(A)
ans = 0
for k, v in C.items():
    if v < k:
        ans += v
    elif v > k:
        ans += (v-k)
print(ans)
