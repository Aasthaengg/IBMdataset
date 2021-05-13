from collections import Counter

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    A[i] += A[i-1]
    A[i] %= M

CA = Counter(A)
ans = 0
for value in CA.values():
    ans += value * (value - 1) // 2
print(ans)