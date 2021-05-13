from decimal import Decimal
X = int(input())
cnt = 0
yokin = Decimal(100)
while X>yokin:
    yokin += (yokin/100).to_integral(rounding='ROUND_FLOOR')
    cnt += 1
print(cnt)
