from functools import reduce

mod = 10**9+7

def modcumprod(*args):
    return reduce(lambda x, y: x*y%mod, args)

n, k = map(int, input().split())
a = list(map(int, input().split()))

if n == k:
    print(modcumprod(*a))
elif max(a) < 0 and k % 2 == 1:
    a.sort(reverse=True)
    print(modcumprod(*a[:k]))
else:
    a.sort(key=abs, reverse=True)
    res = 1
    cnt_neg = 0
    pos1 = neg1 = 0
    for e in a[:k]:
        res *= e
        res %= mod
        if e > 0:
            pos1 = e
        else:
            cnt_neg += 1
            neg1 = e

    if res == 0 or cnt_neg % 2 == 0:
        print(res)
    else:
        pos2 = neg2 = 0
        for e in a[k:]:
            if e > 0 and not pos2:
                pos2 = e
            elif e < 0 and not neg2:
                neg2 = e
            if pos2 and neg2:
                break
        if abs(pos1 * pos2) < abs(neg1 * neg2) and pos1:
            res *= pow(pos1, -1, mod)
            res *= neg2
            res %= mod
        else:
            res *= pow(neg1, -1, mod)
            res *= pos2
            res %= mod
        print(res)
