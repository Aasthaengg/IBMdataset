def resolve():
    import math
    A, B, C, D = [int(i) for i in input().split()]
    A -= 1
    LCMCD = C * D // math.gcd(C, D)
    ans = (B - B // C - B // D + B // LCMCD) - \
          (A - A // C - A // D + A // LCMCD)
    print(ans)


resolve()
