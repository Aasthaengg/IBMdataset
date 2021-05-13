#C - Multiplication 3 WA
import decimal 
A,B = input().split()
A,B = map(decimal.Decimal,[A,B])
ans = A*B
print(int(ans))