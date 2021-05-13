import decimal
Deci = decimal.Decimal
A,B = input().split()
x,y = Deci(A),Deci(B)
ans = int(x*y)
print(ans)