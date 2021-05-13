N, M = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
N1 = 1
M1 = 1
cnt = 1
while True:
    cnt += 1
    if cnt <= N:
        N1 *= cnt
    if cnt <= M:
        M1 *= cnt
    N1 %= mod
    M1 %= mod
    if (cnt > M) and (cnt > N):
        break

if N == M - 1:
    ans = N1 * M1

elif N - 1 == M:
    ans = N1 * M1

elif N == M:
    ans = N1 * M1 * 2

else:
    ans = 0
ans %= mod
print(ans)