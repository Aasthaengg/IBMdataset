def z_algorithm(s):  # O(|S|)
    """
    SとS[i:]のLCP(longest common prefix: 最長共通接頭辞の長さ) Z[i]を計算し、Zを返す
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    i = 1
    j = 0
    while i < n:
        while i + j < n and s[j] == s[i + j]:
            j += 1
        z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k < j and k + z[k] < j:
            z[i + k] = z[k]
            k += 1
        i += k
        j -= k
    return z

# ---------------------- #

n = int(input())
s = input()

ans = 0
for i in range(n):
    Z = z_algorithm(s[i:])
    for j in range(len(Z)):
        if Z[j] > j:
            ans = max(ans, j)
        else:
            ans = max(ans, Z[j])

print(ans)
