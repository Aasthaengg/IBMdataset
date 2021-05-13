import sys

readline = sys.stdin.readline

MOD = pow(10,9)+7

def combinations(n,k):
    global fac, finv
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

def main():
    global fac, finv
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))
    A.sort()

    MAX_NUM = N + 1

    fac  = [0 for _ in range(MAX_NUM)]
    finv = [0 for _ in range(MAX_NUM)]
    inv  = [0 for _ in range(MAX_NUM)]

    fac[0]  = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,MAX_NUM):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD

    summax = 0
    summin = 0
    for i in range(N-K+1):
        j = N-i
        tmp = combinations(j-1, K-1)
        summax += A[j-1] * tmp
        summin += A[i] * tmp
        #print('max:{}, min:{}'.format(A[j-1] * tmp, A[i] * tmp))
    ans = (summax - summin) % MOD
    print(ans)


if __name__ == "__main__":
    main()
