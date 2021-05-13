from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
tmp = 0
for i in range(N):
    A[i] += tmp
    A[i] %= M
    tmp = A[i]

c = Counter(A)
ans = 0
for k, v in c.items():
    if k == 0:
        ans += v
    ans += v * (v-1) // 2

print(ans)
