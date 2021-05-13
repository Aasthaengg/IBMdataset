def abc126c():
    import math
    n, k = map(int, input().split())
    ans = 0.0
    for i in range(1, n + 1):
        v = max(0, math.ceil(math.log2(k / i)))
        ans += math.pow(0.5, v)
    print(ans/n)


abc126c()