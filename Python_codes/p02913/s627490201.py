def z_algo(S):
    N = len(S)

    A = [0] * N
    A[0] = N
    i = 1
    j = 0

    while i < N:
        while i + j < N and S[j] == S[i + j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while N - i > k < j - A[k]:
            A[i + k] = A[k]
            k += 1
        i += k
        j -= k
    return A


N = int(input())
S = input()

ans = 0
for i in range(N - 1):
    A = z_algo(S[i:])
    for idx, length in enumerate(A):
        if idx + 1 > length:
            ans = max(ans, length)

print(ans)
