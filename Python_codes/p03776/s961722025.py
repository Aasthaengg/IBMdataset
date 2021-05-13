from functools import reduce

def binom(n, r):
    if n < r or n < 0 or r < 0: return 0
    
    if n - r < r: r = n - r
    if r == 0: return 1
    elif r == 1: return n

    numerator = [n - r + 1 + k for k in range(r)]  # (n-r+1)*(n-r+2)*...*(n-1)*n
    denominator = [1+ k for k in range(r)]         # 1*2*...*(r-1)*r

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


N, A, B = map(int, input().split())
*V, = map(int, input().split())
V = sorted(V, reverse=True)
ans = 0
ways = 0
if len(set(V[:A])) == 1:
    ans = V[0]
    n = V.count(ans)
    for i in range(A, min(B, n)+1): ways += binom(n, i)
else:
    ans = sum(V[:A]) / A
    min_num = min(V[:A])
    n_min = V.count(min_num)
    n_min_lst = V[:A].count(min_num)
    ways = binom(n_min, n_min_lst)
print(ans)
print(ways)