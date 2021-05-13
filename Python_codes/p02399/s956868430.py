from decimal import Decimal, ROUND_DOWN

a, b = map(int,input().split())

print("{} {} {:.8f}".format(int(a/b),a%b,Decimal(a/b)))
