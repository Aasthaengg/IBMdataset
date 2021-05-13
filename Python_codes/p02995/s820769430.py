A, B, C, D = map(int, input().split())


def gcd(x, y):
    if x > y:
        x, y = y, x
    while y != 0:
        tmp = x % y
        x = y
        y = tmp
    return x
    
A = A - 1
lcm_CD = C * D // gcd(C, D)
cnt_B = B - (B//C + B//D) + (B//lcm_CD)
cnt_A = A - (A//C + A//D) + (A//lcm_CD)

ans = cnt_B - cnt_A
print(ans)