def Z_algo(S):
    N = len(S)
    result = 0
    c = 0
    Z = [0]*N
    for i in range(1, N):
        l = i - c
        if (i + Z[l] < c + Z[c]):
            Z[i] = Z[l]
        else:
            j = max(0, c + Z[c] - i)
            if i + j >= N:
                j = min(j, N-i-1)
            while(S[j] == S[i + j]):
                j += 1
                if i + j >= N:
                    break
            Z[i] = j
            c = i
        result = max(result, min(Z[i], i))
    return result

L = int(input())
P = list(input())
ans = 0

for k in range(L):
    ans = max(ans, Z_algo(P[k:]))

print(ans)