from scipy.misc import comb
# > comb(n, k, exact = True)

nn, kk = map(int, input().split())
r = nn - kk
b = kk
p = 10 ** 9 + 7

# for nCk calculation -----------------------
'''
factorial = [0] * (nn + 1)
factorial[0] = 1
for i in range(nn):
    factorial[i + 1] = factorial[i] * (i + 1) % p
# 逆元


def cmb(n, k):
    # if (n == 1 or k == 1):
    if (n == 0 or k == 0):
        return 1
    if (n < 0 or k < 0):
        return 0

    return factorial[n] * pow(factorial[n - k], p - 2, p) * pow(factorial[k], p - 2, p) % p

'''
# ---------------------------------------
for i in range(1, kk + 1):
    ans = comb(r + 1, i, exact=True) * comb(b - 1, i - 1, exact=True) % p

    #ans = (cmb(r + 1, i) * cmb(b - 1, i - 1)) % p
    print(ans)


# https://img.atcoder.jp/abc132/editorial.pdf
