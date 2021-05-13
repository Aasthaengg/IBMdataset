def gcd(x, y):
    x = abs(x)
    y = abs(y)

    if x < y:
        x, y = y, x

    while y:
        x, y = y, x % y

    return x


N = int(input())
seen = dict()
zeroes = 0
MOD = 10 ** 9 + 7
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        zeroes += 1  # 虚無鰯の数
        continue

    if a < 0 or a == 0 and b < 0:
        a, b = -a, -b
    if b <= 0:
        a, b = -b, a
        flip = 1
    else:
        flip = 0
    g = gcd(a, b)
    a //= g
    b //= g  # 正規化
    if (a, b) not in seen:
        seen[(a, b)] = [0, 0]

    seen[(a, b)][flip] += 1


out = 1
for v in seen:
    a, b = seen[v]  # 連想配列中の値を取り出す[n(a, b) vs. n(-b, a)]
    out *= (pow(2, a, MOD) + pow(2, b, MOD) - 1)
    out %= MOD
out -= 1  # 1個も選ばない場合

out += zeroes  # 虚無鰯の数を足す
out %= MOD
print(out)
