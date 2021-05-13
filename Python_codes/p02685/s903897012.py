def create_array(n: int, r: int, mod, mod2):
    m_ls = [1] * (r + 1)

    for i, j in zip(range(n, 0, -1), range(1, r + 1)):
        m_ls[j] = (m_ls[j - 1] * i * pow(j, mod2, mod)) % mod
    return m_ls


def main():
    n, m, k = map(int, input().split())

    _mod = 998244353
    _mod2 = 998244351

    # res_x = m * ((m-1) ** (n-1-x)) * comb(n-1, x)
    # x:0, 2, ... , k
    # xをk->0とすると(m-1) ** (n-1-x)は少しずつかけていける

    comb_ar = create_array(n-1, k, _mod, _mod2)
    _z = (m - 1) ** (n - 1 - k)
    res = m * _z * comb_ar[k]
    res %= _mod

    if k > 0:
        for x in range(1, k + 1):
            _z *= m - 1
            _z %= _mod
            res += m * _z * comb_ar[k - x]
            res %= _mod

    print(res)


main()
