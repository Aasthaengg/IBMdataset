N = int(input())
S = input()

ans = 0
while S:
    Z = [0] * N
    i = 1
    j = 0
    while i < N:
        while i + j < N and S[j] == S[i + j]:
            j += 1

        Z[i] = j

        if j == 0:
            i += 1
        else:
            k = 1
            while k < j and k + Z[k] < j:
                Z[i + k] = Z[k]
                k += 1
            i += k
            j -= k    

    ans = max(ans, max(min(i, z) for i, z in enumerate(Z)))

    S = S[1:]
    N -= 1

print(ans)