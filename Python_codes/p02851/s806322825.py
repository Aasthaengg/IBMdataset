from collections import defaultdict

n, k = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (n + 1)
for i in range(n):
    S[i+1] = S[i] + A[i]

f = lambda n: (S[n] - n) % k
C = defaultdict(int)
ans = 0
for i in range(n):
    C[f(i)] += 1
    j = i - k + 1
    if 0 <= j:
        C[f(j)] -= 1
    ans += C[f(i+1)]
print(ans)