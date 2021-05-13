N = int(input())
A = tuple(map(int, input().split()))


def f(pm):
    ans, s = 0, 0
    for a in A:
        s += a
        if s * pm <= 0:
            d = abs(s - pm)
            ans += d
            s += d * pm
        pm *= -1
    return ans


print(min(f(1), f(-1)))
