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

def abc132d_blue_and_red_balls():
    n, k = map(int, input().split())
    for i in range(1, k+1):
        if n+1-k< i:
            print(0)
            continue
        print((cmb(n+1-k, i)*cmb(k-1, i - 1))%(pow(10, 9)+7))
abc132d_blue_and_red_balls()