N, K = map(int, input().split())
S = list(input())

diff = []
ans = 0
for i in range(N-1):
  if S[i] != S[i+1]:
    diff += [i]
  else:
    ans += 1

print(min(N-1, ans+2*min(K, len(diff))))