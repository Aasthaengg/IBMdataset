import math


a, b = list(map(int, input().split()))

ans = -1

for i in range(0, 1251):
    tax_a = int(i * 0.08)
    tax_b = int(i * 0.1)

    if tax_a == a and tax_b == b:
        ans = i
        break

print(ans)
