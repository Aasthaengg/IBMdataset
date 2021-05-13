from collections import Counter

N, K = map(int, input().split())
A = list(map(lambda s: int(s) % K, input().split()))

cumAm1 = [1] + A
for i in range(1, N + 1):
    cumAm1[i] = (-1 + cumAm1[i - 1] + cumAm1[i]) % K

counts = Counter()
ans = 0
for i in range(N + 1):

    if i >= K:
        counts[cumAm1[i - K]] -= 1

    cur = cumAm1[i]
    ans += counts[cur]

    counts[cur] += 1

print(ans)
