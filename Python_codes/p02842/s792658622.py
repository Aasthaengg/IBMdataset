def main():
    from decimal import Decimal
    x = Decimal(input())
    for i in range(60000):
        if int(Decimal(i)*Decimal('1.08'))==x:
            return i
    return ':('
print(main())