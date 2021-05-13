from scipy.misc import comb

def prime_factorize_dict(N):
    d = dict()
    for n in range(2, N + 1):
        while not n & 1:
            d[2] = d.get(2, 0) + 1
            n >>= 1
        f = 3
        while f * f <= n:
            if not n % f:
                d[f] = d.get(f, 0) + 1
                n //= f
            else:
                f += 2
        if n != 1:
            d[n] = d.get(n, 0) + 1
    return {k:v for k, v in d.items() if v > 1}

d = prime_factorize_dict(int(input()))

l = [0] * 5
for p, k in d.items():
    if k < 4:
        index = 0
    elif k < 14:
        index = 1
    elif k < 24:
        index = 2
    elif k < 74:
        index = 3
    else:
        index = 4
    l[index] += 1

# 2, 4, 4
total = l[0] * comb(sum(l[1:]), 2, exact=True) + comb(sum(l[1:]), 3, exact=True) * 3
# 4, 14
total += l[1] * sum(l[2:]) + comb(sum(l[2:]), 2, exact=True) * 2
# 2, 24
total += sum(l[0:3]) * sum(l[3:]) + comb(sum(l[3:]), 2, exact=True) * 2
# 74
total += l[4]

print(total)
