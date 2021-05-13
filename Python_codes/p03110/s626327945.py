from decimal import Decimal
def main():
    n = int(input())
    xu = [input().split() for _ in range(n)]
    c = Decimal("0")
    for x,u in xu:
        if u == "JPY":
            c += Decimal(x)
        else:
            c += Decimal(x)*Decimal("380000.0")
    print(c)
    
if __name__ == "__main__":
    main()