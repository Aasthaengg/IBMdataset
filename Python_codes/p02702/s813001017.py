from functools import reduce

def binom(n, r):
    if n < r or n < 0 or r < 0: return 0
    
    if n - r < r: r = n - r
    if r == 0: return 1
    elif r == 1: return n

    numerator = [n - r + 1 + k for k in range(r)]  # (n-r+1)*(n-r+2)*...*(n-1)*n
    denominator = [1 + k for k in range(r)]         # 1*2*...*(r-1)*r

    # reduce prod(numerator)//prod(denominator)
    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    
    # calculate nCr
    return reduce(lambda x, y: x*y, numerator)

S = input()
cnt = [0] * 2019; cnt[0] += 1
t = 0
for i, s in enumerate(S[::-1]):
    t += int(s) * pow(10, i, 2019); t %= 2019
    cnt[t] += 1
ans = 0
for i in range(2019):
    if cnt[i] >= 2: ans += binom(cnt[i], 2)
print(ans)