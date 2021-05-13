from decimal import Decimal, ROUND_HALF_UP

n = int(input())
x = list(map(int,input().split()))
a = Decimal(sum(x) / n).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
ans = 0

for i in range(n):
    ans += (x[i] - a) ** 2

print(ans)