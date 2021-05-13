def GCD(x, y):
  # 最大公約数
    if x < y:
        x, y = y, x
    while True:
        r = x % y
        if r == 0:
            return y
        x, y = y, r


def calc_DCD_LCM(x, y):
  # 最大公約数
    gcd = GCD(x, y)
  # 最小公倍数
    lcm = int(x*y/gcd)
    return(gcd, lcm)


while True:
    try:
        x, y = list(map(int, input().split()))
        gcd, lcm = calc_DCD_LCM(x, y)
        print('{0} {1}'.format(gcd, lcm))
    except:
        exit(0)
