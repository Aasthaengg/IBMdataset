def main():
    from decimal import Decimal
    a, b, c = (Decimal(i) for i in input().split())
    if a.sqrt() + b.sqrt() < c.sqrt():
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
