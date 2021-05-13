def resolve():
    N = int(input())
    X = list(map(int, input().split()))
    av = sum(X)/N
    def _round(x, d=0):
        import math
        p = 10 ** d
        return math.floor(x*p)/p if (x*p)%1 < 0.5 else math.ceil(x*p)/p
    P = round(av)
    ans = 0
    for x in X:
        ans += (x-P)**2
    print(ans)

if '__main__' == __name__:
    resolve()