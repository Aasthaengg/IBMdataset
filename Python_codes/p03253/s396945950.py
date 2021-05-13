# from scipy.misc import comb

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def solve(n,m):
    maxdiv = int(m**0.5)
    l = []
    tmp = 2
    num = 0
    while tmp <= maxdiv:
        if m % tmp == 0:
            m /= tmp
            num += 1
        else:
            tmp += 1
            if num != 0:
                l.append(num)
                num = 0
    if m != 1:
        l.append(1)
    res = 1
    for div in l:
        tmp = cmb(n+div-1,div)%(10**9+7)
        res = res * tmp % (10**9+7)
    return int(res)
        

if __name__ == '__main__':
    n,m = map(int,input().split())
    print(solve(n,m))