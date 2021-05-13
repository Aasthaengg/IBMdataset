from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
ans = 0
for k, v in counter.items():
    if v < k:
        ans += v
    elif v > k:
        ans += (v-k)
print(ans)