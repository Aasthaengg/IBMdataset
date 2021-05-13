from decimal import Decimal
n=int(input())
List=list(map(int,input().split()))
add=0
for i in List:
    add+=Decimal(1/i)
print(Decimal(1/add))