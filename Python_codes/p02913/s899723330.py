def z_algo(s):
    """Z-algorithm O(|S|)

    Args:
        s (str): 対象文字列
    
    Returns:
        list: lcp配列 (z[i]: sとs[i:]の最長共通接尾辞の長さ)
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    i, j = 1, 0
    while i < n:
        while i + j < n and s[j] == s[i+j]:
            j += 1
        z[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while i + k < n and k + z[k] < j:
            z[i+k] = z[k]
            k += 1

        i += k
        j -= k

    return z


n = int(input())
s = input()

res = 0
for i in range(n-1):
    z = z_algo(s[i:])
    for j in range(n-i):
        if z[j] <= j and res < z[j]:
            res = z[j]

print(res)