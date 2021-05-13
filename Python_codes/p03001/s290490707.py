from decimal import Decimal
w, h, x, y = map(int, input().split())
print("{:.9f}".format(Decimal(w)*Decimal(h)*Decimal(0.5)), int(2*x==w and 2*y==h))