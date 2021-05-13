from decimal import Decimal,ROUND_HALF_UP
n,d = map(int,input().split())
x = (n+d*2)//(d*2+1)
print(x)