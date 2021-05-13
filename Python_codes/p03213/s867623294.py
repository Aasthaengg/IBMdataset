n = int(input())
def count_factors(n, factors):
    factors.setdefault(2, 0)
    while n%2 == 0:
        factors[2] += 1
        n //=2

    for f in range(3, int(n**0.5)+ 1, 2):
        factors.setdefault(f, 0)
        while n%f == 0:
            factors[f] += 1
            n //= f
    if n != 1:
        factors.setdefault(n, 0)
        factors[n] += 1


cf = {1: 1}
for i in range(1, n+1):
    count_factors(i, cf)

# 約数が75個になるように選ぶ
ans = 0
c25 = 0
c15 = 0
c5 = 0
c3 = 0
c2 = 0
for v in cf.values():
    if v >= 74:
        ans += 1
    if v >= 24:
        c25 += 1
    if v >= 14:
        c15 += 1
    if v >= 4:
        c5 += 1
    if v >= 2:
        c3 += 1
    if v >= 1:
        c2 += 1

ans += c25 *(c3 - 1)
ans += c15 *(c5 - 1)
ans += c5 * (c5-1) * (c3-2)//2
print(ans)
