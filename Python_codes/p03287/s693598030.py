from collections import Counter
N, M = map(int, input().split())
A = tuple(map(int, input().split()))

cumA = [0] * (N + 1)
for i in range(N):
    cumA[i + 1] = A[i] + cumA[i]
    cumA[i + 1] %= M

c = Counter(cumA)
ans = 0
for k, v in c.items():
    ans += v * (v - 1) // 2

print(ans)
