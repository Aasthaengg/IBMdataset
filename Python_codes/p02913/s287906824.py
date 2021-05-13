def z_algo(s):
    res = [0] * len(s)
    res[0] = len(s)
    i = 1
    j = 0
    while i < len(s):
        while i + j < len(s) and s[j] == s[i + j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < len(s) and k + res[k] < j:
            res[i + k] = res[k]
            k += 1
        i += k
        j -= k
    return res


n = int(input())
s = input()

ans = 0
for i in range(n):
    res = z_algo(s[i:])
    for i, lcp in enumerate(res):
        ans = max(ans, min(lcp, i))
print(ans)
