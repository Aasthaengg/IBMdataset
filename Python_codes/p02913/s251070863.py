def z_al(s):
    le = len(s)
    res = [0 for i in range(le)]
    i, j = 1, 0
    while i < le:
        while i + j < le and s[i + j] == s[j]:
            j += 1
        res[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < le and res[k] + k < j:
            res[i + k] = res[k]
            k += 1
        i += k
        j -= k
    return res
n = int(input())
s = input()
ans = 0
for i in range(n):
    s2 = s[i:]
    res = z_al(s2)
    for j in range(len(s2)):
        ans = max(ans, min(res[j], j))
print(ans)
