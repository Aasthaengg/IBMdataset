from decimal import Decimal

w, h, x, y = map(int, input().split())

print(Decimal(w*h/2), 1 if w == 2*x and h == 2*y else 0)