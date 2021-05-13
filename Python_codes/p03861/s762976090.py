# from decimal import Decimal
a, b, c = map(int, input().split())
print(b//c - a//c if a%c != 0 else b//c - a//c +1)