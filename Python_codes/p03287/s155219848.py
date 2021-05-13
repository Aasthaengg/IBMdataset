from collections import defaultdict
N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
S = [0] * (N+1)
m = defaultdict(int)
ans = 0
for i in range(N):
    S[i+1] = (S[i] + A[i]) % M
for s in S:
    ans += m[s]
    m[s] += 1
print(ans)
