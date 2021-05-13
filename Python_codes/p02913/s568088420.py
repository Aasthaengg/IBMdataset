def Z_algorithm(s):
    n = len(s)
    Z = [0] * n  # z[i] = sum(s[0::n - i], s[i::n])
    Z[0] = n
    i, j = 1, 0
    while i < n:
        # 共通部分を見つけるパート
        while i + j < n and s[j] == s[i + j]:
            j += 1
        Z[i] = j

        if j == 0:
            i += 1
            continue
        # 計算の再利用パート
        # k + Z[k] < j なら再利用できる
        k = 1
        while k < j and k + Z[k] < j:
            Z[i + k] = Z[k]
            k += 1
        # k個先まで見たのでk個先にバトンを渡す
        i += k
        j -= k
    return Z


def solve(k):
    a = Z_algorithm(s[k:])
    ans = 0
    for i in range(n - k):
        ans = max(ans, min(i, a[i]))
    return ans


n, s = int(input()), input()
print(max(solve(i) for i in range(n)))
