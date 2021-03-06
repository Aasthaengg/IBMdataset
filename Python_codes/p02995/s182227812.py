import math
A, B, C, D = map(int, input().split())

lcm = C * D // math.gcd(C, D)

def num_multi(num, lb, ub): # [lb, ub]にnumの倍数がいくつあるのかを返す
    lR = lb // num
    lQ = lb % num

    uR = ub // num
    # uQ = ub % num

    ans = uR - lR
    if lQ == 0:
        ans += 1

    return ans

print((B-A+1) - num_multi(C, A, B) - num_multi(D, A, B) + num_multi(lcm, A, B))
