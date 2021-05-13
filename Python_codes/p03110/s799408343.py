from decimal import Decimal

N = int(input())
X = []
U = []
total = Decimal(0)
for _ in range(N):
    x, u = input().split()
    d = Decimal(x)
    if u == "JPY":
        total += d
    else:
        total += d * 380000
print(total)



