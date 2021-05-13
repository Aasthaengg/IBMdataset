import sys
from decimal import Decimal

def main():
    n = int(sys.stdin.readline().strip())
    money = Decimal('100000')
    rate = Decimal('1.05')
    
    for _ in range(n):
        money *= rate
        if money % 1000:
            money = money // 1000 * 1000 + 1000

    print(money)
    
if __name__ == '__main__':
    main()