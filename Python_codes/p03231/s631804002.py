# https://atcoder.jp/contests/agc028/tasks/agc028_a

n, m = map(int, input().split())
s = input()
t = input()

def gcd(x, y): #GCD
    # greatest_common_divisor
    if x < y:
        x, y = y, x
    if y == 0:
        return 0
    if x % y == 0:
        return y
    return gcd(y, x % y)

def lcm(x, y): #LCM
    # lowest_common_multiple
    return x * y // gcd(x, y)

l = lcm(n, m)
d = gcd(n, m)
n //= d
m //= d

for i in range(d):
    if s[i * n] != t[i * m]:
        print(-1)
        break
else:
    print(l)