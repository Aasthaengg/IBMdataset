def resolve():
    L, R = list(map(int, input().split()))
    MOD = 2019
    if R - L >= 2019:
        print(0)
        return
    import itertools
    ans = float("inf")
    for i, j in itertools.combinations(list(range(L, R+1)), 2):
        ans = min(ans, i*j%MOD)
    print(ans)

if '__main__' == __name__:
    resolve()