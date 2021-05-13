# Z-Algorithm
#############################################################
def z_algo(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    i, j = 1, 0
    while i < n:
        while i + j < n and s[j] == s[i + j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < n and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i += k
        j -= k
    return z
#############################################################

N = int(input())
S = input()

ans = 0
for i in range(N):
    z = z_algo(S[i:])
    # j = 0,1,...,N-i-1
    # zのindexは0,1,...,N-i-1
    for j in range(N - i):
        # z[j]>jの時、部分文字列が重なってしまう
        if z[j] <= j:
            ans = max(ans, z[j])

print(ans)
