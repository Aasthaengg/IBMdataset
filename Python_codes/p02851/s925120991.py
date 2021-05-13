from collections import defaultdict

def gets():
  return list(map(int, input().split()))

N, K = gets()
A = gets()

S = [0] * (N + 1)
for i in range(N):
  S[i + 1] = (S[i] + A[i] - 1) % K

cnt = defaultdict(int)
ans = 0
cnt[0] += 1
for i in range(1, N+1):
  if i - K >= 0:
    cnt[S[i - K]] -= 1
  ans += cnt[S[i]]
  cnt[S[i]] += 1

print(ans)
