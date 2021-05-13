import math

A, B, C, D = map(int, input().split())


def not_multiple_of_c_and_d(x: int, c: int, d: int):
    lcm_cd = c * d // math.gcd(c, d)
    c_no_baisu = x // c
    d_no_baisu = x // d
    cd_no_baisu = x // lcm_cd
    return x - (c_no_baisu + d_no_baisu - cd_no_baisu)


ans = not_multiple_of_c_and_d(B, C, D) - not_multiple_of_c_and_d(A-1, C, D)
print(ans)
