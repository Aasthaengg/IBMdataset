nums = sorted(list(map(int, input().split())), reverse=True)


def gcd(mx, mi):
    if mi == 0:
        return mx
    amari = mx % mi
    return gcd(mi, amari)

print(gcd(nums[0], nums[1]))

