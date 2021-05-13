N, M = map(int, input().split())
if abs(N - M) > 1:
    print(0)
    exit()
mod = 10 ** 9 + 7
ans = 1
for i in range(1, N + 1):
    ans = ans * i % mod
for i in range(1, M + 1):
    ans = ans * i % mod
print(ans * 2 % mod if N == M else ans)