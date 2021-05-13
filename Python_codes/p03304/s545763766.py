import decimal
n,m,d=map(int,input().split())
print(decimal.Decimal(((2**min(1,d))*(n-d)*(m-1))/(n**2)))
