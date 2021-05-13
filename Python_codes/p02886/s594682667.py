def resolve():
    N = int(input())
    D = list(map(int, input().split()))
    ans = 0
    import itertools
    for x, y in itertools.combinations(D, 2):
        ans += x*y
    print(ans)

if '__main__' == __name__:
    resolve()