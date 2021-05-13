
def comb(n, max_k, mod):
    """
    (n,k) := n個からk個選ぶ組み合わせ
    k = 0~max_Kまでを計算して返す
    """
    res = [1]*(max_k+1)
    t = 1
    for i in range(max_k+1):
        res[i] *= t
        t *= n-i
        t %= mod

    n = reduce(lambda x,y: (x*y)%mod, range(1,max_k+1), 1)
    n = modinv(n, mod)

    for i in reversed(range(max_k+1)):
        res[i] *= n
        res[i] %= mod
        n *= i
        n %= mod
    return res

N,P = map(int,input().split())

A = map(int,input().split())

evens = 0
odds = 0

for a in A:
    if a%2:
        odds += 1
    else:
        evens += 1


cnt = 0
if P == 0:
    comb = 1
    cnt = 1
    for n in range(2,odds+1,2):
        comb *= (odds+2-n)*(odds+1-n)
        comb //= n*(n-1)
        cnt += comb
else:
    comb = odds
    cnt = odds
    for n in range(3,odds+1,2):
        comb *= (odds+2-n)*(odds+1-n)
        comb //= n*(n-1)
        cnt += comb

print(2**evens * cnt)