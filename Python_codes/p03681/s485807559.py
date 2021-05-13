def fac(n, p):
    ret = 1
    for i in range(2, n + 1):
        ret = ret * i % p
    return ret

N, M = [int(x) for x in input().split()]
p = 10 ** 9 + 7
if abs(N - M) >= 2:
    ans = 0
elif N == M:
    ans = 2 * fac(N, p) * fac(M, p) % p
else:
    ans = fac(N, p) * fac(M, p) % p

print(ans)