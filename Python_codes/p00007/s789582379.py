from math import ceil

DEBT = 100000
DIGITS = 1000
INTEREST_RATE = 1.05

def calc_debt(n):
    d = DEBT // DIGITS
    while n > 0:
        d = ceil(d * INTEREST_RATE)  # 借金の小数点以下を切り捨て
        n  -= 1
    return d * DIGITS

n = int(input())
print(calc_debt(n))

