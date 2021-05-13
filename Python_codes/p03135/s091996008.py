from decimal import *

def main():
    t, x = map(int, input().split())
    print(Decimal(t) / Decimal(x))

main()