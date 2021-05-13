
M = int(input())
T = input()
ans = 0
for l in range(M):
    i, j = 1, 0
    S = T[l:]
    N = M-l
    Z = [0]*N
    Z[0] = N
    while i < N:
        while i+j < N and S[j] == S[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k+Z[k] < j:
            Z[i+k] = Z[k]
            k += 1
        i += k
        j -= k
    for i in range(N):
        ans = max(ans, min(i, Z[i]))

print(ans)
