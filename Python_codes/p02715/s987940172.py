import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
def resolve():
    N, K = lr()
    MOD = pow(10, 9)+7
    lst = [0]*K
    klst = [0]*K
    for k in range(K, 0, -1):
        lst[k-1] = pow(K//k, N, MOD)
        for i in range(2, K//k+1):
            lst[k-1] -= lst[i*k-1]
        klst[k-1] = k*lst[k-1]
    print(sum(klst)%MOD)
resolve()