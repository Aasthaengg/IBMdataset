N = int(input())
S = input()


def z_algorithm(s):
    n = len(s)
    lcpls = [0] * n  # Longest common prefix length
    lcpls[0] = n

    l = r = 1
    while l < n:
        while (r < n) and (s[r - l] == s[r]):
            r += 1

        if l == r:
            l += 1
            r += 1
            continue

        lcpls[l] = r - l

        k = 1
        while (l + k < r) and (lcpls[k] < r - l - k):
            lcpls[l + k] = lcpls[k]
            k += 1
        l += k

    return lcpls


ans = 0
for i in range(N):
    X = S[i:]
    Z = z_algorithm(X)

    for j, z in enumerate(Z):
        if j >= z:
            ans = max(ans, z)

print(ans)
