import decimal
decimal.getcontext().prec=50
a,b,x=map(int,input().split())
a=decimal.Decimal(a)
b=decimal.Decimal(b)
print(int(b/x)-int((a+x-1)/x)+1)