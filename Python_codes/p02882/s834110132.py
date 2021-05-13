import decimal
import math
a,b,x=map(int,input().split())
num1=a*a*b-x
if (a*a*b)/2<x:
    num2=decimal.Decimal((num1*2)/(a*a))
    num3=decimal.Decimal(math.sqrt(decimal.Decimal((a*a)+decimal.Decimal(num2*num2))))
    num4=decimal.Decimal((a*a+decimal.Decimal(num3*num3)-decimal.Decimal(num2*num2))/decimal.Decimal(2*decimal.Decimal(a*num3)))
    ans=math.degrees(math.acos(num4))
else:
    num2=decimal.Decimal((x*2)/(a*b))
    num3=decimal.Decimal(math.sqrt(decimal.Decimal((b*b)+decimal.Decimal(num2*num2))))
    num4=decimal.Decimal((num2*num2+decimal.Decimal(num3*num3)-decimal.Decimal(b*b))/decimal.Decimal(2*decimal.Decimal(num2*num3)))
    ans=math.degrees(math.acos(num4))
print(ans)
