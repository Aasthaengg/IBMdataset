N = int(input())
MOD = 10 ** 9 + 7
A = [1] * 64
A[6] = A[9] = A[33] = 0
for _ in range(N-3):
    B = [0] * 64
    for p in range(256):
        i = p >> 2
        j = p & 63
        b = ((i == 6) or (i == 9) or (i == 33)
            or (j == 6) or (j == 9) or (j == 33)
            or (p & 207 == 9) or (p & 243 == 33))
        if not b:
            B[j] = (B[j] + A[i]) % MOD
    A[:] = B[:]
res = 0
for a in A:
    res = (res + a) % MOD
print(res)