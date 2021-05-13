n, m = map(int, input().split())
delta = abs(n - m)

mod = 10 ** 9 + 7
N = 10 ** 5 + 5
bikkuri = [0 for i in range(N)]
bikkuri[0] = 1
gyaku = [0 for i in range(N)]
gyaku[0] = 1
for i in range(1, N):
    bikkuri[i] = (i * bikkuri[i - 1]) % mod
    gyaku[i] = pow(bikkuri[i], mod - 2, mod)

if delta > 1:
    print(0)
else:
    if n > m:
        ans = bikkuri[n] * bikkuri[m]
    elif m > n:
        ans = bikkuri[m] * bikkuri[n]
    else:
        ans = 2 * bikkuri[m] * bikkuri[n]
    print(ans % mod)
