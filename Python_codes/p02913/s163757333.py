def zarg(N, S):
    Z = [0] * N
    Z[0] = N
    i = 1
    j = 0
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        i += k
        j -= k
    M = 0
    for i in range(1,N):
        M = max(M, min(Z[i], i))
    return M

N = int(input())
S = input()
ans = 0
for i in range(N):
    s = S[i:]
    ans = max(ans, zarg(N-i, s))
print(ans)