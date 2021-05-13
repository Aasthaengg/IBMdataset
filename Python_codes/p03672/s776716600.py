S = list(input())
N = len(S) // 2
for i in range(1, N):
  A = S[:(N-i)]
  B = S[N-i:2 * (N-i)]
  if A == B:
    ans = 2 * (N-i)
    break
print(ans)