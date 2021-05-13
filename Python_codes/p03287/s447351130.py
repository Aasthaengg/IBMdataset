from collections import Counter


N, M = map(int, input().split())
A = list(map(int, input().split()))
A1 = [a % M for a in A]

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = (S[i] + A1[i]) % M

T = sorted(S)
C = Counter(S)
key = list(C.keys())
ans = 0
for i, s in enumerate(S):
    C[s] -= 1
    ans += C[s]

print(ans)
