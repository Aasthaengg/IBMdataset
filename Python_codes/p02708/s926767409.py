N, K = map(int, input().split())
A = [i for i in range(N+1)]
S = [0] * (N+2)
mod = 10 ** 9 + 7

for right in range(1, N+2):
    S[right] = S[right-1] + A[right-1]

total = S[N+1]
ans = 0
for left in range(N+2):
    total -= A[max(left-1, 0)]
    if (N+1) - left >= K:
        ans += (total - S[(N+1)-left] + 1) % mod

print(ans % mod)