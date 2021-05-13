import decimal

n = int(input())

ans = 0
for i in range(n):
    x, v = input().split()
    if v == 'JPY':
        ans += int(x)
    else:
        a = decimal.Decimal(x)
        b = decimal.Decimal(380000)
        c = a * b
        ans += c

print(ans)