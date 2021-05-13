from decimal import Decimal
N, M = map(int, input().split())
i = 1
ans = 0
time = 1900 * M + 100 * (N - M)
while True:
    ex = time * i *  ((1/2) ** M) * ((1 - (1/2) ** M) ** (i - 1))
    if ex < 0.000000001:
        break
    ans += ex
    i += 1
print(Decimal(str(ans)).quantize(0, rounding="ROUND_HALF_UP"))