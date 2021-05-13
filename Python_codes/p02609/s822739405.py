N = 2 * 10 ** 5
n = int(input())
x = input()

def popcount(n):
    res = 0
    while n > 0:
        res += n & 1
        n >>= 1
    return res

f = [0] * (N + 1)
for i in range(1, N + 1):
    m = i
    while True:
        f[i] += 1
        p = popcount(m)
        m %= popcount(m)
        if m == 0:
            break

px = x.count('1')
m01 = 0
m10 = 0
for c in x:
    b = int(c)
    m01 = (2 * m01 + b) % (px + 1)
    if px - 1 != 0:
        m10 = (2 * m10 + b) % (px - 1)

for i, c in enumerate(x):
    if c == '0':
        m = m01 + pow(2, n - i - 1, px + 1)
        m %= px + 1
        print(f[m] + 1)
    elif px - 1 == 0:
        print(0)
    else:
        m = m10 - pow(2, n - i - 1, px - 1)
        m %= px - 1
        print(f[m] + 1)