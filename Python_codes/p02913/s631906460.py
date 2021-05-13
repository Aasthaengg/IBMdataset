def z_algolithm(S, x):
    length = len(S) - x
    A = [0]*length
    B = [0]
    i = 1; j = 0
    while i < length:
        while i+j < length and S[x+j] == S[x+i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        B.append(min(j, i))
        k = 1
        while k < length - i  and k + A[k] < j :
            A[i+k] = A[k]
            k += 1
        i += k
        j -= k
    ans = max(B)
    return ans


n = int(input())
S = input()

candidates = []
for i in range(n):
    candidates.append(z_algolithm(S, i))

print(max(candidates))