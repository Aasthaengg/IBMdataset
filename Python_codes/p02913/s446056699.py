n = int(input())
s = input()
"""
def lcs(s, t):
    ls, lt = len(s), len(t)
    dp = [[0] * (lt+1) for _ in range(ls+1)]
    for i in range(ls):
        for j in range(lt):
            #prev = dp[i+1][j+1]
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
    return dp[ls][lt]
"""
def z_algorithm(s):
    ls = len(s)
    Z = [0] * ls
    Z[0] = ls
    i, j = 1, 0
    while i < ls:
        while i + j < ls and s[j] == s[i+j]:
            j += 1
        Z[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < ls and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        i += k
        j -= k
    return Z

ans = 0
for i in range(n):
    #print(s[i:])
    z = z_algorithm(s[i:])
    for j, zj in enumerate(z):
        if j+1 > zj:
            ans = max(ans, zj)
    #print(z)
print(ans)