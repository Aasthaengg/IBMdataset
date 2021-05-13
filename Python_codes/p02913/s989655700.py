def z_algorithm(s):
    res = [0 for _ in range(len(s))]
    res[0] = len(s)
    i, j = 1, 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i + j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k < j and k + res[k] < j:
            res[i + k] = res[k]
            k += 1
        i += k
        j -= k
    return res

N = int(input())
S = input()

res = 0

for i in range(N):
    z = z_algorithm(S[i:])
    for j in range(N - i):
        res = max(res, min(j, z[j]))

print(res)