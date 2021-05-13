from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

S = [0]*(N+1); S[0] = 0;
d = defaultdict(int); d[0] = 1;
for i in range(1, N+1):
  S[i] = (S[i-1] + A[i-1]) % M
  d[S[i]] += 1
  
ans = 0
for key, val in d.items():
  ans += val * (val - 1) // 2
print(ans)